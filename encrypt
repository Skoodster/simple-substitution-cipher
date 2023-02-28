
import string

def encrypt_file(filename):
    alphabet = string.ascii_lowercase
    cipher_alphabet = "qwertyuiopasdfghjklzxcvbnm"

    with open(filename, "r") as input_file:
        with open("encrypted_" + filename, "w") as output_file:
            # read the input file one line at a time
            for line in input_file:
                encrypted_line = ""
                for char in line:
                    if char.lower() in alphabet:
                        encrypted_char = cipher_alphabet[alphabet.index(char.lower())]
                        if char.isupper():
                            encrypted_chat = encrypted_char.upper()
                        encrypted_line += encrypted_char
                    else:
                        encrypted_line += char
                output_file.write(encrypted_line)
    print("Encryption complete. Encrypted file saved as encrypted_"+filename)

filename = input("Enter the filename of the text file to encrypt: ")
encrypt_file(filename)