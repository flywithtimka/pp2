import os

def list_all(path):
    
    all_items = os.listdir(path)
    return all_items

path = r'C:\PP2\pp2\lab06\dirandfile'
all_items = list_all(path)
print("All items (Directories and Files):", all_items)