x=input("Enter a string")
n=int(input("Enter number"))
def caeser(x,n):
    enc=""
    for i in range (len(x)):
        if (x[i].islower()):
            enc+= chr((ord(x[i]) + n - 97) % 26 + 97)
        if (x[i].isupper()):
            enc+= chr((ord(x[i]) + n - 65) % 26 + 65)
    return enc
print(caeser(x,n))
