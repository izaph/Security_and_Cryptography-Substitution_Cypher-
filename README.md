# 8-bit Substitution Cipher CLI

A Python-based command-line application that implements a substitution cipher. This tool can encrypt and decrypt any file by mapping its 8-bit ASCII character set to a randomized alternative set.

## Implementation Approach

1.  **Character Mapping:** The application handles the full 8-bit ASCII range (0-255). It uses a fixed "seed" with Python's `random` module to shuffle the byte values, ensuring that the encryption is reproducible (the same key is used for both locking and unlocking).
2.  **Efficiency:** I used the built-in `bytes.translate()` method. This allows the program to process large files (like the 10KB+ requirement) almost instantaneously by swapping bytes at the memory level.
3.  **CLI Design:** The interface uses the `argparse` library, which allows the user to provide arguments in any order (e.g., `-e` can come before or after the input file name).

## How to Run

### 1. Requirements
- Python 3.12 or higher installed.

### 2. Encryption
To encrypt a file, use the `-e` flag, the input file name, and the `-o` flag for the output:
```bash
python cipher.py -e test_input.txt -o encrypted.bin