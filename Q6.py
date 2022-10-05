txt = input('Write something: ')
aux = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', \
            'g', 'h', 'i', 'j', 'k', 'l', \
            'm', 'n', 'o', 'p', 'q', 'r', \
            's', 't', 'u', 'v', 'w', 'y', \
            'x', 'z', 'A', 'B', 'C', 'D', \
            'E', 'F', 'G', 'H', 'I', 'J', \
            'K', 'L', 'M', 'N', 'O', 'P', \
            'Q', 'R', 'S', 'T', 'U', 'V', \
            'W', 'X', 'Y', 'Z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special = ['', '!', '"', '#', '$', '%', '&', '(', ')', \
           '*', '+', ',', '-', '.', '/', ':', ';', '<', \
           '=', '>', '?', '@', '[', ']', '^', '_', '`', \
           '{', '|', '}', '~']
print(list in alphabet)
for aux in range(txt.__len__()):
    if txt[aux] in alphabet:
        print(txt[aux], ', is an alphabet')
    elif txt[aux] in digit:
        print(txt[aux], ', is a digit')
    elif txt[aux] in special:
        print(txt[aux], ', is a special character')
