import string

def decryptText(ciphertext, shift):
    if not isinstance(ciphertext, str):
        raise ValueError("Text must be a string.")
    if not isinstance(shift, int) or shift < 0 or shift > 25:
        raise ValueError("Shift must be an integer between 0 and 25.")
    
    # Initializing the empty array
    tempText = []
    for char in ciphertext:
        if char in string.ascii_uppercase:
            # Convert it into uppercase letters
            decryptedCharactor = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            tempText.append(decryptedCharactor)
        elif char in string.ascii_lowercase:
            # Convert it into lowercase letters
            decryptedCharactor = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            tempText.append(decryptedCharactor)
        else:
            tempText.append(char)
    return ''.join(tempText)

def findDecryptionCode(ciphertext):
    if not isinstance(ciphertext, str):
        raise ValueError("Cipher text must be a string.")
    
    for shift in range(1, 26):  # Test shifts 1 to 25
        try:
            tempText = decryptText(ciphertext, shift)
            print(f"Shift {shift}: {tempText}")
        except ValueError as e:
            print(f"Error {shift}: {e}")

def main():
    # Example ciphertext
    ciphertext = ("VZ SDSKLWER LKJGD HE LEWWR EWTECSDF KSEJ V NZ BHG BS PBJSDFSDG "
                  "HSKDJHB MBJWUIR BCJSGF JJAGUWRG JRUI LKUOIQWUROIW JHKJHKJO "
                  "ZMNCBXMV LKJLWE")
    
    try:
        print("Decrypting the cryptogram...")
        findDecryptionCode(ciphertext)
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
