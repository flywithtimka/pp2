def unique(lst):
    unique_list = [] 
    for item in lst: 
        if item not in unique_list: 
            unique_list.append(item) 
    return unique_list 

print(unique([1, 2, 3, 3, 2, 1, 4, 5]))  
print(unique([7, 7, 7, 7, 7])) 
print(unique([10, 20, 10, 30, 40, 20]))  