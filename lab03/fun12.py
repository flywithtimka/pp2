def palindrome(s):
    cleaned_s = ''.join(e.lower() for e in s if e.isalnum())  
    return cleaned_s == cleaned_s[::-1]

print(palindrome("madam"))  
print(palindrome("racecar"))  
print(palindrome("hello"))  