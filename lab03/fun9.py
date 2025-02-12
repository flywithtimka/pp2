import math  
def sphere_volume(r):
    return (4/3) * math.pi * r**3 
r = float(input("Enter a number:"))    
print(f"{sphere_volume(r)}")
print(sphere_volume(1))
print(sphere_volume(3)) 
print(sphere_volume(5))