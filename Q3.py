y = 'try'
while y.__len__()) != 4:
    y = input('Type a year with four digits: ')
    if (y.__len__()) != 4:
        print('please write a four digit number: ')

y = int(y)
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(y, "is leap year")
        else:
            print(y, "is not leap year")
    else:
        print(y, "is leap year")