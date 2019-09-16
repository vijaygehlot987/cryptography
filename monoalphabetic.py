key={'A':'a','B':'b',
     'C':'c','D':'d',
     'E':'e','F':'f',
     'G':'g','H':'h',
     'I':'i','J':'j',
     'K':'k','L':'l',
     'M':'m','N':'n',
     'O':'o','P':'p',
     'Q':'q','R':'r',
     'S':'s','T':'t',
     'U':'u','V':'v',
     'W':'w','X':'x',
     'Y':'y','Z':'z'}
def monoalphabetic(text):
    text=str(text)
    x=[]
    for l in text:
        x.append(key.get(l,l))
    print(''.join(x))
print(monoalphabetic("SUPERVISOR"))
