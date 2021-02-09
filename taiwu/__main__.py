import os
import shutil
import sys
from datetime import datetime

save_files_path = '/mnt/d/programs/steam/steamapps/common/The Scroll Of Taiwu/The Scroll Of Taiwu Alpha V1.0_Data/SaveFiles'
backup_files_path = '/mnt/c/Users/Administrator/Documents/TaiWuHuiJuan/Backup'
log_file_path = os.path.join(backup_files_path, "log.txt")
log_file = open(log_file_path, 'a')


def log(msg: str):
    print(msg)
    print(msg, file=log_file)


def cmd_help():
    print('Example: ')
    print(' 1. taiwu commit               备份游戏存档')
    print('    taiwu c                    short version')
    print(' 2. taiwu log                  查看备份状态')
    print('    taiwu l                    short version')
    print(' 3. taiwu reset                加载最近的游戏存档')
    print('    taiwu r                    short version')


def get_backup_files(path: str) -> list:
    return [name for name in os.listdir(path) if name.find('Date_') == 0]


def get_backup_groups(path: str) -> set:
    groups = set()
    files = get_backup_files(path)
    for file in files:
        if file.find('Date_') != -1:
            groups.add(file[:file.find('.')])
    return groups


def cmd_commit():
    files = get_backup_files(save_files_path)
    for file in files:
        from_path = os.path.join(save_files_path, file)
        to_path = os.path.join(backup_files_path, "{}.{}".format(file, datetime.now().strftime("%Y-%m-%d-%H-%M-%S")))
        log('from: {}\nto: {}'.format(from_path, to_path))
        shutil.copytree(from_path, to_path)
        log('done: {}'.format(to_path))


def cmd_log():
    groups = get_backup_groups(backup_files_path)
    files = get_backup_files(backup_files_path)
    for group in groups:
        target = max([file for file in files if file.find(group + ".") == 0])
        print('{} : {}'.format(group, target))


def cmd_reset():
    groups = get_backup_groups(backup_files_path)
    files = get_backup_files(backup_files_path)
    for group in groups:
        target = max([name for name in files if name.find(group + ".") == 0])
        from_path = os.path.join(backup_files_path, target)
        to_path = os.path.join(save_files_path, group)
        shutil.rmtree(to_path)
        shutil.copytree(from_path, to_path)
        print('{} : load to {}'.format(group, target))


def cli():
    if len(sys.argv) == 2:
        if sys.argv[1] in ['commit', 'c']:
            cmd_commit()
            return
        elif sys.argv[1] in ['reset', 'r']:
            cmd_reset()
            return
        elif sys.argv[1] in ['log', 'l']:
            cmd_log()
            return
    cmd_help()
