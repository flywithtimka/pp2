import os

def list_files(path):
    files = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]
    return files

path = r'C:\PP2\pp2\lab06\dirandfile'
files = list_files(path)
print("Files:", files)