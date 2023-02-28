# simple-substitution-cipher
 
 
The program prompts the user to enter the filename of a textfile which is then opened and read line by line. For each character in the line, the program checks the letter and looks up its corresponding encrypted character in the substitution cipher. Encrypted files are saved as 'encrypted_filename' (Where 'filename' is the name of your original file) under the same directory as the original file.

If you are running the code from an IDE, put the file you are encrypting in the same directory as the program and set the IDE's working directory the same as the file and program's directory.
 
 
 
 
I set the substitution cipher to be rather easy to crack, currently the cipher is:

OG:

abcdefghijklmnopqrstuvwxyz

ENCRYPTED:

qwertyuiopasdfghjklzxcvbnm

However, you could change the cipher alphabet on Line6 and it (should) work fine 
