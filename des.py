from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
def encrypt(pt,key):
 key=key.encode()
 cipher=DES.new(key,DES.MODE_ECB)
 padd=pad(pt.encode(),DES.block_size)
 ct=cipher.encrypt(padd)
 return ct
def decrypt(ct,key):
 key=key.encode()
 cipher=DES.new(key,DES.MODE_ECB)
 decrypted=cipher.decrypt(ct)
 pt=unpad(decrypted,DES.block_size)
 return pt.decode()
key="12345678"
pt=input("enter the palintext:")
encryption=encrypt(pt,key)
print(encryption)
decrption=decrypt(encryption,key)
print(decrption)