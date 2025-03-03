def count_case_letters(s):
    upper_count = sum(map(str.isupper, s))  
    lower_count = sum(map(str.islower, s)) 
    return upper_count, lower_count

string = input("Enter the string:")
upper, lower = count_case_letters(string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)