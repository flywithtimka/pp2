def write_list_to_file(file_path, my_list):
    try:
        
        with open(file_path, 'w') as file:
            
            for item in my_list:
                file.write(f"{item}\n")
        print(f"List successfully written to {file_path}")
    except IOError:
        print(f"An error occurred while writing to the file {file_path}.")

my_list = ["apple", "banana", "cherry", "date"]
file_path = r'C:\PP2\pp2\lab06\dirandfile\file.txt'  
write_list_to_file(file_path, my_list)