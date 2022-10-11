### Input of the Month
m =int (input('Please input a month: '))
### Input of the Day
d =int (input('Please input a day: '))
### Input of the Year
y = int (input('Please input a year: '))

### Calculation for the specific day of the week
y0 = y - (14-m) // 12
x = y0 + y0//4 - y0//100 + y0//400
m0 = m + 12 * ((14-m)//12) - 2
d0 = (d + x + (31*m0)//12) % 7

### If to separete each day of the week
if d0 == 0:
    print('This date corresponds to a Sunday')
elif d0 == 1:
    print('This date corresponds to a Monday')
elif d0 == 2:
    print('This date corresponds to a Tuesday')
elif d0 == 3:
    print('This date corresponds to a Wednesday')
elif d0 == 4:
    print('This date corresponds to a Thursday')
elif d0 == 5:
    print('This date corresponds to a Friday')
elif d0 == 6:
    print('This date corresponds to a Saturday')
else:
    print('ERROR')
