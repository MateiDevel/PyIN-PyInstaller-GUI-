import subprocess

def build(path, isNoconsole, name, onefile):
    subprocess.run(f'pyinstaller {path} {isNoconsole} {name} {onefile}')