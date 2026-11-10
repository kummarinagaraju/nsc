
def encrypt(text,k,alphabet):
    result=""
    for ch in text:
     if ch.isalpha():
        index=alphabet.index(ch)
        result+=k[index]
     else:
      result+=ch
    return result
def decrypt(text,k,alphabet):
    result=""
    for ch in text:
        if ch.isalpha():
            index=k.index(ch)
            result+=alphabet[index]
        else:
          result+=ch
    return result             

text=input("enter the text").upper()
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k="QWERTYUIOPASDFGHJKLZXCVBNM"
cipher=encrypt(text,k,alphabet)
print("cipher text",cipher)
pt=decrypt(cipher,k,alphabet)
print("plain text",pt)

