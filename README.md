# Substitution Cipher

To make this substitution ciper I used a Python based command line application and Visual Studio Code as IDE. It is made to encrypt and/or decrypt any file by mapping its 8-bit ASCII characters to a randomized alternative set. Using "generate_test.py" one can create a text file (around 13KB) containing Lorem ipsum. I used it for testing the code, but any text file can be used with this code. 


## Implementation Approach

   **Character Mapping:** The application handles the full 8-bit ASCII range (0-255). It uses a fixed "seed" with Python's `random` module to shuffle the byte values, ensuring that the encryption is reproducible (the same key is used for both locking and unlocking).
   **Efficiency:** I used the built-in `bytes.translate()` method. This allows the program to process large files (like the 10KB+ requirement) almost instantaneously by swapping bytes at the memory level.

###  Requirements
- Python 3.12 or higher installed.

## How to Run

-> After downloading "cipher.py" you can obtionally download "generate_test.py" if you need a file to test on, but any other text file works just fine

-> Open the folder containing the files in Visual Studio Code (or an other IDE that supports Python)

-> Make sure that you have succesfully installed Python 3.12 or higher

-> If you're going to use "generate_test.py" bash in the terminal the following line: python generate_test.py  
   If you have your own file, skip this step.

-> To encrypt the file run in the terminal: python cipher.py -e file_name.txt -o encrypted.bin 

-> To decrypt the file, run the following in the terminal: python cipher.py -d encrypted.bin -o decrypted.txt


### Example 

I used "genereate_test.py" to generate a .txt file containing 40 paragraphs of Lorem ipsum (around 13KB). After running the following comand lines:
    python generate_test.py
    python cipher.py -e test_input.txt -o encrypted.bin
    python cipher.py -d encrypted.bin -o decrypted.txt

I ended up having the following files: test_input.txt (the file used for encrypting and decrypting), encrypted.bin (the encrypted file) and decrypted.txt (the decrypted file). You can see them attached
    
