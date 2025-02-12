import math
def degree(deg):
    return (deg * math.pi)/180
deg = float(input("Enter the degree:"))  
print(f"{"The number in radians is:"}{degree(deg)}")  