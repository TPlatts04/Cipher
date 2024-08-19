ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():
    print("\nWelcome to Tom's Cipher Application")
    cipherText = input("What is the message you would like to encrypt/decrypt? ")
    offsetKey = int(input("What offset would you like to encrypt/decrypt by? "))
    encrypt_decrypt = input("Would you like to encrypt or decrypt? ").lower()
    match encrypt_decrypt:
        case "encrypt":
            encrypt(cipherText, offsetKey)
        case "decrypt":
            decrypt(cipherText, offsetKey, -1)
        case "_":
            raise ValueError("Invalid option, please try again...")

def cipher(message, offset, direction=1):
    new_text = ""
    index = 0
    for i in message.lower():
        if direction == 1:
            if i.isalpha():
                index = ALPHABET.find(i)
                new_text += ALPHABET[(index + offset) % len(ALPHABET)]
                print(i, index)
            else:
                new_text += i
        else:
            if i.isalpha():
                index = ALPHABET.find(i)
                new_text += ALPHABET[(index - offset) % len(ALPHABET)]
                print(i, index)
            else:
                new_text += i
    print(new_text)

def encrypt(message, offset):
    return cipher(message, offset)

def decrypt(message, offset, direction):
    return cipher(message, offset, direction)

if __name__ == "__main__":
    main()