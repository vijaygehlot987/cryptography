def vernam(text,key):
    res=""
    x=0
    for i in text:
        res=res+chr(ord(i)^ord(key[x]))
        x=x+1
    return res
a=input("enter text")
enckey=input("enter key")
enc=vernam(a,enckey)
print(enc)
dec=vernam(enc,enckey)
print(dec)
    
        
        
