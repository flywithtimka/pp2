def create_files():
    for i in range(26):
        
        letter = chr(65 + i)  
        
        file_name = f"{letter}.txt"
        
        
        with open(file_name, 'w') as file:
            file.write(f"This is file {file_name}")
        
        print(f"{file_name} has been created.")

create_files()