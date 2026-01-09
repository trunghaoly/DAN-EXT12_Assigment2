def input_data():
    '''
    Get user input for Length (L), Depth (D), and Sides (N).
    '''
    
    # Input initial length
    L = int(input('Enter initial length (L): '))

    # Input recursion depth
    D = int(input('Enter recursion depth (D): '))

    # Input number of sides
    N = int(input('Enter number of sides (N): '))
    
    return (L,D,N)
