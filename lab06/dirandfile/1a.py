import os

def list_directories(path):
    
    directories = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    return directories

path = r'C:\PP2\pp2\lab06\dirandfile'
directories = list_directories(path)
print("Directories:", directories)