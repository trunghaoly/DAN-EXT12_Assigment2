# Step 1: Decrypt text
def decrypt_char(char, key_id, shift1, shift2):
    
    if key_id in ('5', '6'):
        return char
    
    if key_id == '1':                                       
        shift = - (shift1 * shift2)
        base_char = 'a'
    elif key_id == '2':                                     
        shift = shift1 + shift2
        base_char = 'a'
    elif key_id == '3':                                     
        shift = shift1
        base_char = 'A'
    elif key_id == '4':                                     
        shift = - (shift2 ** 2)
        base_char = 'A'
    else:                                                  
        return char 
        
    base_index = ord(base_char)
    current_index = ord(char) - base_index
    new_index = (current_index + shift) % 26
    return chr(base_index + new_index)


def decrypt_file(shift1, shift2, input_file="encrypted_text.txt", key_file="encryption_keys.txt", output_file="decrypted_text.txt"):

    with open(input_file, 'r', encoding='utf-8') as encrypted_file:
        encrypted_text = encrypted_file.read()
    with open(key_file, 'r', encoding='utf-8') as keys_file:
        keys_text = keys_file.read()

    if len(encrypted_text) != len(keys_text):
        return False

    decrypted_text = "".join([
        decrypt_char(encrypted_text[i], keys_text[i], shift1, shift2) 
        for i in range(len(encrypted_text))
    ])

    with open(output_file, 'w', encoding='utf-8') as decrypted_file: 
        decrypted_file.write(decrypted_text)
        
    return True