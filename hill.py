key=[]
print("enter the 2*2 key matrix:")
for i in range(2):
    row=list(map(int,input().split()))
    key.append(row)
pt=input("enter the palain text")
if len(pt)%2!=0:
    pt+="x"
ct=""    
for i in range(0,len(pt),2):
    p1=ord(pt[i])-ord('A')
    p2=ord(pt[i+1])-ord('A')
    c1=(key[0][0]*p1+key[0][1]*p2)%26
    c2=(key[1][0]*p1+key[1][1]*p2)%26
    ct+=chr(c1+ord('A'))
    ct+=chr(c2+ord('A'))
print(ct)
inkey=[]
print("entter the inverse key:")
for i in range(2):
    row=list(map(int,input().split()))
    inkey.append(row)
ptt="" 
for i in range(0,len(ct),2):
    p1=ord(ct[i])-ord('A')
    p2=ord(ct[i+1])-ord('A')
    c1=(inkey[0][0]*p1+inkey[0][1]*p2)%26
    c2=(inkey[1][0]*p1+inkey[1][1]*p2)%26
    ptt+=chr(c1+ord('A'))
    ptt+=chr(c2+ord('A'))
print(pt)