import string

def decrypt_file(filename):
    key = "qwertyuiopasdfghjklzxcvbnm"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    inverse_key = str.maketrans(key,alphabet)

    with open(filename,'r') as input_file:
        encrypted_text = input_file.read()
    decrypted_text = encrypted_text.translate(inverse_key)
    with open("decrypted_" +filename, 'w') as output_file:
        output_file.write(decrypted_text)
    print(f"Decryption complete. Decrypted text saved as decrypted_filename")
    
filename = input("Enter the filename of the encrypted file: ")
decrypt_file(filename)