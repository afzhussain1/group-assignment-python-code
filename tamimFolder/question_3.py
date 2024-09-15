# def encrypt(text, key):
#     encrypted_text = ""  

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
#             encrypted_text+ = char  # 'encrypted_text += chr(shifted)'

#     return encrypted_text 

# # Error: Missing key value and original_code
# key = ???????????????  # Missing key value
# original_code = "Hello World!"  # Example original code

# encrypted_code = encrypt(original_code, key)
# print(encrypted_code)



def encrypt(text, key):
    encrypted_text = ""  
    #for loop condition
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
              # if condition to check the code
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
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Added non-alphabet 
# invokig the code
    return encrypted_text

#define the function
def decrypt(text, key):
    decrypted_text = ""  
 # for loop condition
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
             #condtion for lowercase
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
            decrypted_text += char 
      #invoking the funtion value
    return decrypted_text

key = 3  # demmy key value
originalCode = "demmy key value" 

encryptedCode = encrypt(originalCode, key)
print(f"Output Encrypted Code: {encryptedCode}")

decrypted_code = decrypt(encryptedCode, key)
print(f"Output Decrypted Code: {decrypted_code}")
