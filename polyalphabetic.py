def encrypted(pt,key):
    ct=""
    key=key.upper()
    key_index=0
    for char in pt:
       if char.isalpha:
          shift=ord(key[key_index%len(key)])-ord('A')
          if char.isupper:
           enr=chr((ord(char)-ord('A')+shift)%26+ord('A'))
          else:
           enr=chr((ord(char)-ord('a')+shift)%26+ord('a'))
          ct+=enr
          key_index+=1
       else:
         ct+=char
    return ct
def decrypted(ct,key):
    pt=""
    key=key.upper()
    key_index=0
    for char in ct:
       if char.isalpha:
          shift=ord(key[key_index%len(key)])-ord('A')
          if char.isupper:
           denr=chr((ord(char)-ord('A')-shift)%26+ord('A'))
          else:
           denr=chr((ord(char)-ord('a')-shift)%26+ord('a'))
          pt+=denr
          key_index+=1
       else:
         pt+=char
    return pt
pt=input("enter the text").upper()
key=input("enter the key ").upper()
encryption=encrypted(pt,key)
print("cipher text=",encryption)      
decryption=decrypted(encryption,key)
print("plain text after decryption is =",decryption)