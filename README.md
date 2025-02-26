# Caesar_encryption
Caesar Cipher Program
Purpose: This program encrypts and decrypts text using the Caesar cipher algorithm. The user can input a message and a shift value to perform encryption or decryption.

Code Explanation:

caesar_cipher_encrypt(text, shift):

Encrypts the input text by shifting each character by the specified shift value.

Handles both uppercase and lowercase letters, preserving non-alphabetic characters.

caesar_cipher_decrypt(text, shift):

Decrypts the input text by calling the encryption function with a negative shift value.

main():

Provides a user interface to choose between encryption, decryption, or quitting the program.

Prompts the user to enter a message and a shift value.

Displays the encrypted or decrypted message based on the user's choice.

Example Usage:

Encrypting the text "Hello, World!" with a shift of 3 results in "Khoor, Zruog!".

Decrypting the text "Khoor, Zruog!" with a shift of 3 results in "Hello, World!".
