# taiwu-love-me-once-more

The Scroll of Taiwu: simple tool for backup game. Note that I only want to use this tool for Gong Fu learning but not a
perfect life

## Install

### Use Source Code

clone the source code of memory.

```shell
git clone git@github.com:zhenghaohui/taiwu-love-me-once-more.git
```

jump into the source code directory

```shell
cd taiwu-love-me-once-more
```

Edit the path of your game path & your backup path

```shell
vim taiwu/__main__.py

# Edit:
save_files_path = '/mnt/d/programs/steam/steamapps/common/The Scroll Of Taiwu/The Scroll Of Taiwu Alpha V1.0_Data/SaveFiles'
backup_files_path = '/mnt/c/Users/Administrator/Documents/TaiWuHuiJuan/Backup'
```

install using python3:

```shell
python3 setup.py install

# or for wsl user, you might need to run under 'sudo'

sudo python3 setup.py install
```

### Start

try enter:

```shell
taiwu
```