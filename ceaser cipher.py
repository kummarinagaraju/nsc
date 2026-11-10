def encrypted(pt,shift):
    ct=""
    for char in pt:
       if char.isalpha():
         
          if char.isupper():
           enr=chr((ord(char)-ord('A')+shift)%26+ord('A'))
          else:
           enr=chr((ord(char)-ord('a')+shift)%26+ord('a'))
          ct+=enr
         
       else:
         ct+=char
    return ct
def decrypted(ct,key):
    return encrypted(ct,key)
pt=input("enter the text").upper()
shift=int(input("enter the shift key "))
encryption=encrypted(pt,shift)
print("cipher text=",encryption)      
decryption=decrypted(encryption,-shift)
print("plain text after decryption is =",decryption)