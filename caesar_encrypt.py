from numpy.core.defchararray import upper


def caesar_cipher_encrypt(text, shift):

    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

#this function below decrypts the text
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("caesar cipher algorithm")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt or (Q to quit): ").upper()

        if choice ==  'Q':
            break
        elif choice not in ['E', 'D']:
            print("Invalid input. Please just stick to 'E' to encrypt, 'D' to decrypt and 'Q' to quit the program")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift you want: "))

        if choice == 'E':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print("Encrypted Message:", encrypted_message)
        elif choice == 'D':
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print("Decrypted Message:", decrypted_message)

    print("THANKS FOR USING CAESAR ENCRYPTION!")

if __name__== "__main__":
    main()

