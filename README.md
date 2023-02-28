# simple-substitution-cipher

-----------------------------------------------------------------------------------------------------------
 
The program prompts the user to enter the filename of a textfile which is then opened and read line by line. For each character in the line, the program checks the letter and looks up its corresponding encrypted character in the substitution cipher. Encrypted files are saved as 'encrypted_filename' (Where 'filename' is the name of your original file) under the same directory as the original file. The decryption programs do the same thing but reversed, yea! Decrypted files are saved as 'decrypted_encrypted_filename'. Keep encrypting and decrypting and you're gonna have a long ah filename

-----------------------------------------------------------------------------------------------------------
Running the program:
-----------------------------------------------------------------------------------------------------------
When inputting the filename, you must include the .txt extension at the end of the filename, Ex: filename.txt

	Running program via an IDE:
Put the file you are encrypting/decrypting in the same directory as the program and make sure the IDE's working directory is the same as the file and program's directory.

	Running program via the executable:
Same as the IDE really, put file you're encrypting/decrypting and executable under the same directory
 
-----------------------------------------------------------------------------------------------------------
 
I set the substitution cipher to be rather easy to crack, currently the cipher is:

OG:

abcdefghijklmnopqrstuvwxyz

ENCRYPTED:

qwertyuiopasdfghjklzxcvbnm

However, you could change the cipher alphabet and it (should) work fine (maybe idk) If the cipher alphabet is changed in the encryption program, you'll have to change the key for the decryption to correspond with the new alphabet.

-----------------------------------------------------------------------------------------------------------
