#Input of the month
m = int(input('Please input a month: '))
#Input of the day
d = int(input('Please input a day: '))
#list with all days in a month
fm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
      11, 12, 13, 14, 15, 16, 17, 18, 19, 20, \
      21, 22, 23, 24, 25, 26, 27, 28, 29, 30, \
      31]

#test to see if the date input (m + d) belongs to the specific season
if ((m == 12) and (d in fm[20:32])) or (m == (1 or 2)) or ((m == 3) and (d in fm[0:21])):
    print('WINTER')
elif ((m == 3) and (d in fm[20:32])) or (m == (4 or 5)) or ((m == 6) and (d in fm[0:21])):
    print('SPRING')
elif ((m == 6) and (d in fm[20:32])) or (m == (7 or 8)) or ((m == 9) and (d in fm[0:21])):
    print('SUMMER')
else:
    print('AUTUMN')
