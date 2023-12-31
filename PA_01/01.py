def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += ""

    return result


def decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += ""

    return result


while True:
    print("Enter a choice (1-3) ")
    choice = int(input("1.Encrypt\n2.Decrypt\n3.Exit :"))

    if choice == 1:
        text = input("Enter a text :")
        key = int(input("Enter a key :"))
        print("Encrypting...")

        ciphertext = encrypt(text, key)

        print("Cipher text : ", ciphertext)

    elif choice == 2:
        print("Decrypting...")
        print("Plain text : ", decrypt(ciphertext, key))
    elif choice == 3:
        break
    else:
        print("Invalid choice ")


        
