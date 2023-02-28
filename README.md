# simple-substitution-cipher

-----------------------------------------------------------------------------------------------------------
 
The program prompts the user to enter the filename of a textfile which is then opened and read line by line. For each character in the line, the program checks the letter and looks up its corresponding encrypted character in the substitution cipher. Encrypted files are saved as 'encrypted_filename' (Where 'filename' is the name of your original file) under the same directory as the original file.

-----------------------------------------------------------------------------------------------------------

When inputting the filename, you must also include the .txt extension at the end of the filename. Ex: filename.txt

	Running program using an IDE:
Put the file you are encrypting in the same directory as the program and set the IDE's working directory the same as the file and program's directory.

	Running program by running the executable:
Same as the IDE really, put original file and executable under the same directory
 
-----------------------------------------------------------------------------------------------------------
 
I set the substitution cipher to be rather easy to crack, currently the cipher is:

OG:

abcdefghijklmnopqrstuvwxyz

ENCRYPTED:

qwertyuiopasdfghjklzxcvbnm

However, you could change the cipher alphabet on Line6 and it (should) work fine 

-----------------------------------------------------------------------------------------------------------
