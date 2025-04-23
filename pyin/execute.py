import subprocess

def build(path, isNoconsole):
    subprocess.run(f'pyinstaller {path} {isNoconsole}')