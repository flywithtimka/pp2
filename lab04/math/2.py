def trapezoid_area(height, base1, base2):
    return ((base1 + base2) / 2) * height
height = float(input("Enter the height:"))
base1 = float(input("Enter the base 1:"))
base2 = float(input("Enter the base 2:"))

print("Area of trapezoid:", trapezoid_area(height, base1, base2))
