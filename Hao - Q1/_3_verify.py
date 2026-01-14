def compare():
    """
    Verifies if the decrypted text matches the original raw text.
    """

    # Open files for verification
    with    open('raw_text.txt','r',encoding='utf-8') as rawtext, \
            open('decrypted_text.txt','r',encoding='utf-8') as decrypted:
    
        # Read content
        rawdata = rawtext.read()
        decrypteddata = decrypted.read()
    
        # Compare and print result
        if rawdata == decrypteddata:
            print('SUCCESS: The decrypted text matches the original.')
        else:
            print('FAILURE: The content does not match.')