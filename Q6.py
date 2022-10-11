txt = input('Write a character: ') #imput of the program

### List of Alphabetic Characters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', \
            'g', 'h', 'i', 'j', 'k', 'l', \
            'm', 'n', 'o', 'p', 'q', 'r', \
            's', 't', 'u', 'v', 'w', 'y', \
            'x', 'z', 'A', 'B', 'C', 'D', \
            'E', 'F', 'G', 'H', 'I', 'J', \
            'K', 'L', 'M', 'N', 'O', 'P', \
            'Q', 'R', 'S', 'T', 'U', 'V', \
            'W', 'X', 'Y', 'Z']

### List of Numeric Characters
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

### List of Special Characters
special = ['', '!', '"', '#', '$', '%', '&', '(', ')', \
           '*', '+', ',', '-', '.', '/', ':', ';', '<', \
           '=', '>', '?', '@', '[', ']', '^', '_', '`', \
           '{', '|', '}', '~', "'", ' ']

### Adding backslash to the list of special characters
backslash = '\ '
backslash = backslash[0:1]
special.append(backslash)

### Tests to Identify to wich group the character belongs
if txt in alphabet:
    print(txt, ', is an alphabet')
elif txt in digit:
    print(txt, ', is a digit')
elif txt in special:
    print(txt, ', is a special character')
