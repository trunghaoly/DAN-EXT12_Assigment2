import os
from Q1_decrypted import *
from Q1_encrypted import *




# main1
# hint=[]
# text1 = read_file('raw_text.txt')
# s1=int(input('enter a shift1: ')) 
# s2=int(input('enter a shift2: '))
text2, hint = encrypted (text1,s1,s2)
write_file('encrypted.txt',text2)

# main2
text3 = decrypted (text2, s1,s2)
write_file('decrypted.txt',text3)
if text1.strip() == text3.strip():
    print('success')      


             