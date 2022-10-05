d = int(input("Enter an amount of days: "))

y = d // 365
w = (d % 365) // 7
dT = ((d % 365) % 7)

print('Number of years: ', y, '\n')
print('Number of weeks: ', w, '\n')
print('Number of days: ', dT, '\n')