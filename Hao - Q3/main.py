from input import *
from draw import *

def main():
    try:

        # Get input data and execute the drawing 
        L,D,N = input_data()
        setup_and_draw(L,D,N)

    # Handle cases where the user inputs text instead of numbers
    except ValueError:
        print("Input Error: Please enter valid integers.")
    
    # Handle any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    main()
