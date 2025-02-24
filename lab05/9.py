import re

def insert_spaces(text):
    spaced_text = re.sub(r'(?<!^)([A-Z])', r' \1', text)
    return spaced_text
input_text = input("Input your string:")
output_text = insert_spaces(input_text)
print(output_text) 
