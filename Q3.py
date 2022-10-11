### Input of the year
y = int(input('Type a year with four digits: '))

### Verification to find if the year is leap year
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(y, "is leap year")
        else:
            print(y, "is not leap year")
    else:
        print(y, "is leap year")