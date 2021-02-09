import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taiwu",  # Replace with your own username
    version="1.0.0",
    author="zhenghaohui",
    author_email="zhenghaohui.cn@gmail.com",
    description="simple tool for game backup;)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhenghaohui/taiwu-love-me-once-more",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['taiwu=taiwu.__main__:cli'],
    }
)
