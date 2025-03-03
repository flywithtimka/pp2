def all_elements_true(tup):
    return all(tup)  


sample_tuple = (True, 1, "Hello", [1, 2])  
print(all_elements_true(sample_tuple))  

sample_tuple2 = (True, 0, "Hello") 
print(all_elements_true(sample_tuple2)) 