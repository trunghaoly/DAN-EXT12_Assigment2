import os

from Q1_s1_decrypt_text import *
from Q1_s2_encrypt_text import *

# Step 3: verify text
def verify_decryption(original_file="raw_text.txt", decrypted_file="decrypted_text.txt"):
    
    with open(original_file, 'r', encoding='utf-8') as file_raw_text:
        raw_text = file_raw_text.read()  
    with open(decrypted_file, 'r', encoding='utf-8') as file_decrypted_text:
        decrypted_text = file_decrypted_text.read()

    if raw_text == decrypted_text:
        print(f"Verification: SUCCESS! '{original_file}' matches '{decrypted_file}'.")
    else:
        print(f"Verification: FAILED! '{original_file}' does NOT match '{decrypted_file}'.")

def main():
    
    shift1 = int(input("Enter integer value for shift1: "))
    shift2 = int(input("Enter integer value for shift2: "))

    encrypt_file(shift1, shift2)

    decrypt_file(shift1, shift2)

    verify_decryption()
    
if __name__ == "__main__":
    main()