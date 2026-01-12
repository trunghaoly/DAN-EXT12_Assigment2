def input_data():
    while True:
        '''
        Get user input for Length (L), Depth (D), and Sides (N).
        '''
        try:
            
            # Input initial length
            L = int(input('Enter initial length (L): '))

            # Input recursion depth
            D = int(input('Enter recursion depth (D): '))

            # Input number of sides
            N = int(input('Enter number of sides (N): '))
            
            # Check if Length is positive
            if L <=0: 
                print("Caution: The side length must > 0")
                continue

            # Check if Depth is non-negative
            if D < 0:
                print("Caution: The recursion depth must >= 0")
                continue

            # Check if Sides form a polygon
            if N < 3:
                print("Caution: The number of sides must >= 3")
                continue

            return (L,D,N)
        
        except ValueError:
            print("Warning: Must enter a number")    
            
            
