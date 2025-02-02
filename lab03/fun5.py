def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i+1:]
        permute(remaining, answer + ch)

# Example usage
user_input = input("Enter a string: ")
permute(user_input)
