import subprocess

def build(path):
    subprocess.run(f'pyinstaller {path}')