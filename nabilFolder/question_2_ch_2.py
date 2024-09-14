import time
#function defination
def process_string(s):
    number = ''
    letters = ''
    
    #convert string into numbers and letters
    for char in s:
        if char.isdigit():
            number += char
        elif char.isalpha():
            letters += char
    
    # Convert even numbers ASCII code
    processed_number = ''
    for num in number:
        if int(num) % 2 == 0:
            processed_number += str(ord(num))
        else:
            processed_number += num
    
    # Convert uppercase letters to ASCII code
    processed_letters = ''
    for char in letters:
        if char.isupper():
            processed_letters += str(ord(char))
        else:
            processed_letters += char
    
    return processed_number, processed_letters

def get_ascii_codes():
    # even numbers
    even_numbers = ['0', '2', '4', '6', '8']
    ascii_even_numbers = {num: ord(num) for num in even_numbers}
    
    # ASCII codes for uppercase letters
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_uppercase_letters = {char: ord(char) for char in uppercase_letters}
    
    return ascii_even_numbers, ascii_uppercase_letters

# Example
s = "56aAww1984sktr2352700aYmn145ss785fsq31D0"
numbers, letters = process_string(s)

# ASCII codes
ascii_even_numbers, ascii_uppercase_letters = get_ascii_codes()
# to show the output
print(f"Original String: {s}")
print(f"Number String: {numbers}")
print(f"Letters String: {letters}")

print("\nASCII codes for even numbers:")
for num, code in ascii_even_numbers.items():
    print(f"{num}: {code}")

print("\nASCII codes for uppercase letters:")
for char, code in ascii_uppercase_letters.items():
    print(f"{char}: {code}")
