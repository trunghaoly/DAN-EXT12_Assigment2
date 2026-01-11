import os
from Q1_encrypted import *

text1 = read_file('raw_text.txt')
s1=int(input('enter a shift1: ')) 
s2=int(input('enter a shift2: '))

text2, hint = encrypted (text1,s1,s2)
def decrypted (text2,s1,s2):
    text3 =''
    for idx, m in enumerate (text2):
        track=hint[idx]
        if track == 'a':
            b=chr((ord(m)-s1*s2-97)%26+97)
            text3 += b
        elif track =='b':
            b = chr((ord(m)+(s1+s2)-110)%26+110)
            text3 += b
        elif track =='c':
            b = chr((ord(m)+s1-65)%26+65)
            text3 += b
        elif track =='d':
            b=chr((ord(m)-s2*s2-78)%26+78)
            text3 += b
        else:
            text3+=m
    return text3