import math; #diifieHellman
n=int(input("1st prime"))
g=int(input("2nd prime"))
x=int(input("1st private number"))
y=int(input("2nd private number"))
a=pow(n,x)%g #n and g interchangeble
b=pow(n,y)%g
k1=pow(a,x)%g
k2=pow(b,y)%g
if(k1==k2):
    print("Successful")
else: 
    print("unsuccessful")

