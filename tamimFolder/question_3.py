# def encrypt(text, key):
#     encryptedText = ""  

#     for char in text:
#         # Error: Type in method name
#         if char.isalpha():  
#             shifted = ord(char) + key

#             if char.islower():
#                 # Error: Comparison should be with 'z' for lowercas
#                 if shifted > ord("Z"):  #'ord("z")'
#                     shifted -= 26
#                 # Error: missing 'else'
#                 elif shifted < ord("a"):  # elif' and 'ord("a")'
#                     shifted += 26
#             elif char.isupper():
#                 if shifted > ord("Z"):  # Correct 'ord("Z")'
#                     shifted -= 26
#                 # Error: missing 'else' 
#                 elif shifted < ord("a"):  # Should be 'elif' and 'ord("A")'
#                     shifted += 26
#             # Error: Incorrect spelling and missing of character
#             encryptedText+ = char  # 'encryptedText += chr(shifted)'

#     return encryptedText 

# # Error: Missing key value and original_code
# key = ???????????????  # Missing key value
# original_code = "Hello World!"  # Example original code

# encrypted_code = encrypt(original_code, key)
# print(encrypted_code)


# the above code is for errors and their indications and below code is for encrypted and decrypted

def encrypt(text, key):
    # Validate key
    if not isinstance(key, int):
        raise ValueError("Key must be an integer.")
    
    encryptedText = ""
    # for loop to handle the code
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            # if condition
            if char.islower():
                if shifted > ord("z"):
                    shifted -= 26
                elif shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted > ord("Z"):
                    shifted -= 26
                elif shifted < ord("A"):
                    shifted += 26
            encryptedText += chr(shifted)
        else:
            encryptedText += char  # Add non-alphabet characters as they are

    return encryptedText
# function to handle the decryption
def decrypt(text, key):
    # Validate key
    if not isinstance(key, int):
        raise ValueError("Key must be an integer.")
    
    decrypted_text = ""
    # for loop handle the interation of code
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            
            if char.islower():
                if shifted < ord("a"):
                    shifted += 26
                elif shifted > ord("z"):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord("A"):
                    shifted += 26
                elif shifted > ord("Z"):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Added non-alphabet 

    return decrypted_text

try:
    key = 3  # dummy key value
    original_code = "dumm344 325" 

    encrypted_code = encrypt(original_code, key)
    print(f"Output Encrypted Code: {encrypted_code}")

    decrypted_code = decrypt(encrypted_code, key)
    print(f"Output Decrypted Code: {decrypted_code}")

except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
