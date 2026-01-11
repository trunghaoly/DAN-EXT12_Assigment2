def read_file(file_name):
    with open (file_name,'r') as a:
        text1 = a.read()
        return text1

def encrypted (text1,s1,s2):
    hint=[]
    text2=''
    for i in text1:
        if 97<=ord(i)<=109:
            a = chr((ord(i)+s1*s2-97)%26+97)
            text2+=a
            hint.append('a')
        elif 110<=ord(i) <=122:
            a = chr((ord(i)-(s1+s2)-110)%26+110)
            text2+=a
            hint.append('b')
        elif 65<=ord(i)<=77:
            a= chr((ord(i)-s1-65)%26+65)
            text2+=a
            hint.append('c')
        elif 78<=ord(i)<=90:
            a=chr((ord(i)+s2*s2-78)%26+78)
            text2+=a
            hint.append('d')
        else:
            text2+=i
            hint.append('e')
    return text2, hint

def write_file (name,content):
    with open (name,'w') as f:
        f.write(content)