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

day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print('This date corresponds to a ', day[d0])
