from setuptools import setup, find_packages

setup(
    name='pyin',
    version = '0.5',
    packages=find_packages(),
    install_requires=['customtkinter'],
    entry_points={
        'console_scripts' : [
            'pyin = pyin.__main__:main',
        ],
    },
)