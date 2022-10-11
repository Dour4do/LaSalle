### Input of a number of days
d = int(input("Enter an amount of days: "))

### Count of years contained in the amount of days
y = d // 365
### Count of the contained weeks in the amount of days (excluding the years allready calculated)
w = (d % 365) // 7
### Count of the reminder of days
dT = ((d % 365) % 7)

### Print of each value calculated
print('Number of years: ', y, '\n')
print('Number of weeks: ', w, '\n')
print('Number of days: ', dT, '\n')