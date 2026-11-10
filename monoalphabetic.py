alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key="QWERTYUIOPASDFGHJKLZXCVBNM"
pt=input("enter the text").upper()
result=""
choice=input("enter E encryption and D decryption:").upper()
if choice=='E':
    for ch in pt:
        if ch in alpha:
            index=alpha.index(ch)
            result+=key[index]
        else:
            result+=ch
    print("cipher text:",result)            
if choice=='D':
    for ch in pt:
        if ch in alpha:
            index=key.index(ch)
            result+=alpha[index]
        else:
            resultt+=ch
    print("plaintext",result)            
