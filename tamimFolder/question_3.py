def encrypt(text, key):
    encrypted_text = ""  

    for char in text:
        # Error: Type in method name
        if char.isalpha():  
            shifted = ord(char) + key

            if char.islower():
                # Error: Comparison should be with 'z' for lowercas
                if shifted > ord("Z"):  #'ord("z")'
                    shifted -= 26
                # Error: missing 'else'
                elif shifted < ord("a"):  # elif' and 'ord("a")'
                    shifted += 26
            elif char.isupper():
                if shifted > ord("Z"):  # Correct 'ord("Z")'
                    shifted -= 26
                # Error: missing 'else' 
                elif shifted < ord("a"):  # Should be 'elif' and 'ord("A")'
                    shifted += 26
            # Error: Incorrect spelling and missing of character
            encrypted_text+ = char  # 'encrypted_text += chr(shifted)'

    return encrypted_text 

# Error: Missing key value and original_code
key = ???????????????  # Missing key value
original_code = "Hello World!"  # Example original code

encrypted_code = encrypt(original_code, key)
print(encrypted_code)

