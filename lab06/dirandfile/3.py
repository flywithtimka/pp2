import os

def check_path(path):
    
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        directory = os.path.dirname(path)
        print(f"Directory portion: {directory}")
        
        filename = os.path.basename(path)
        print(f"Filename portion: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path = r'C:\PP2\pp2\lab06\dirandfile\3.py'  
check_path(path)