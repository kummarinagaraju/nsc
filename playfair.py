key=input("enter the key: ").upper().replace("J","I")
a="ABCDEFGHIKLMNOPQRSTUVWXYZ"
matrix=""
for ch in key:
    if ch not in matrix and ch in a:
        matrix+=ch
for ch in a:
    if ch not in matrix:
        matrix+=ch
pf=[list(matrix[i:i+5])for i in range(0,25,5)]    
print("playfair matrix")
for row in pf:
    print(row)

def prepare(text):
    text=text.upper().replace("J","I").replace(" ","")
    result=""
    i=0
    while i <len(text):
        a=text[i]
        if i+1<len(text):
            b=text[i+1]
            if a==b:
                result+=a+"X"
                i+=1
            else:
                result+=a+b
                i+=2
        else:
            result+=a+"X"
            i+=1
    return result                  
def find(ch):
    for i in range(5):
        for j in range(5):
            if(pf[i][j]==ch):
                return i,j
choice=input("enter e for encryprion d for decryption").upper()
text=input("enter the text:").upper()
text =prepare(text)
result=""                
for i in range(0,len(text),2):
    a=text[i]
    b=text[i+1]
    r1,c1=find(a)
    r2,c2=find(b)
    if r1==r2:
        if choice=="E":
           result+=pf[r1][(c1+1)%5]
           result+=pf[r2][(c2+1)%5]
        else:
            result+=pf[r1][(c1-1)%5]
            result+=pf[r2][(c2-1)%5]   
    elif c1==c2:        
        if choice=="E":
           result+=pf[(r1+1)%5][c1]
           result+=pf[(r2+1)%5][c2]
        else:
            result+=pf[(r1-1)%5][c1]
            result+=pf[(r2-1)%5][c2]
    else:
     result+=pf[r1][c2]
     result+=pf[r2][c1]
if choice=="E":
    print ("cipher text is :",result)           
else:
    print("plaintextis :",result)    