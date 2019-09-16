import itertools
key = input("Enter Key: ").replace("j", "i")
alphabet = 'abcdefghiklmnopqrstuvwxyz'
a=[]
for x in itertools.chain(key, alphabet):
    if not x in a:
        a.append(x)
matrix = [a[i:i + 5]for i in range(0, 25, 5)]
print("PLAYFAIR CIPHER  "+str(matrix))

