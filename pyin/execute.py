import subprocess

def build(path, isNoconsole, name):
    subprocess.run(f'pyinstaller {path} {isNoconsole} {name}')