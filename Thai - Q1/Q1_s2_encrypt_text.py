# Step 2: encrypt text
def encrypt_char(char, shift1, shift2):
    
    if 'a' <= char <= 'z':
        base_index = ord('a')
        current_index = ord(char) - base_index
        if char <= 'm': 
            shift = shift1 * shift2                    
            key_id = '1'
        else:
            shift = - (shift1 + shift2)                 
            key_id = '2'
        new_index = (current_index + shift) % 26
        return chr(base_index + new_index), key_id
    
    elif 'A' <= char <= 'Z':
        base_index = ord('A')
        current_index = ord(char) - base_index
        if char <= 'M':
            shift = - (shift1)                         
            key_id = '3'
        else:
            shift = shift2 ** 2                        
            key_id = '4'
        new_index = (current_index + shift) % 26
        return chr(base_index + new_index), key_id
    
    elif char == '\n':
        return char, '5'                                
    else:
        return char, '6'                               

def encrypt_file(shift1, shift2, input_file="raw_text.txt", output_file="encrypted_text.txt", key_file="encryption_keys.txt"):
    
    with open(input_file, 'r', encoding='utf-8') as raw_file:
        text = raw_file.read()
    
    encrypted_text = ""
    keys_text = ""
    for char in text:
        new_char, key_id = encrypt_char(char, shift1, shift2)           
        encrypted_text += new_char
        keys_text += key_id
    
    with open(output_file, 'w', encoding='utf-8') as encrypted_file:
        encrypted_file.write(encrypted_text)
    with open(key_file, 'w', encoding='utf-8') as keys_file:
        keys_file.write(keys_text)
    return True