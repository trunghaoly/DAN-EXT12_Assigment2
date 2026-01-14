# Import custom modules
from _1_encrypt import *
from _2_decrypt import *
from _3_verify import *

def main():

    """
    Main function to handle user input and execute the encryption, decryption, and comparison workflow.
    """
    
    # Loop until the user provides valid integer inputs
    while True:
        try:
            shift1 = int(input('shift1: '))
            shift2 = int(input('shift2: '))
            break
        except ValueError:
                print('Error: Please enter valid integers for shifts.')

    # Execute workflow
    try:
        print("--- Encrypting ---")
        key = encrypted_function(shift1, shift2)
        
        print("--- Decrypting ---")
        decrypted_function(key, shift1, shift2)
        
        print("--- Comparing ---")
        compare()

    # Handle potential errors (Missing files, etc.)    
    except FileNotFoundError:
        print('Error: One of the required files was not found')
    except Exception as i:
        print(f'An unexpected error occurred: {i}')

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    main()