import math

def multiply_list(numbers):
    return math.prod(numbers) 

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = multiply_list(numbers)
print("Product of list elements:", result)