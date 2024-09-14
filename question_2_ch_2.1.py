import string

def decryptText(ciphertext, shift):
    # initalizing the empty array
    tempText = []
    for char in ciphertext:
        if char in string.ascii_uppercase:
            # convert it into uppercase letters
            decryptedCharactor = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            tempText.append(decryptedCharactor)
        elif char in string.ascii_lowercase:
            # convert it into lowercase letters
            decryptedCharactor = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            tempText.append(decryptedCharactor)
        else:
            tempText.append(char)
    return ''.join(tempText)

def findDecryptionCode(ciphertext):
    for shift in range(1, 26):  # Test charactors 1 to 25
        tempText = decryptText(ciphertext, shift)
        print(f"Shift {shift}: {tempText}")
        
def main():
    # Example ciphertext
    ciphertext = ("VZ SDSKLWER LKJGD HE LEWWR EWTECSDF KSEJ V NZ BHG BS PBJSDFSDG "
                  "HSKDJHB MBJWUIR BCJSGF JJAGUWRG JRUI LKUOIQWUROIW JHKJHKJO "
                  "ZMNCBXMV LKJLWE")
    
    print("Decrypting the cryptogram...")
    findDecryptionCode(ciphertext)

if __name__ == '__main__':
    main()
