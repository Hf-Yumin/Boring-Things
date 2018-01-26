#"What day is it?"

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']

week = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
    ]

year_i  = raw_input('Year: ')
month_i = raw_input('Month(1-12): ')
day_i   = raw_input('Day(1-31): ')

year    = int(year_i)
month   = int(month_i)
day     = int(day_i)

m = month
y = year

if(m < 3):
    y -= 1
    m += 12

c = int(y / 100)
y = y - 100 * c
x = int(c/4) - 2*c + y + int(y/4) + (26*(m+1) / 10) + day - 1
x = (x%7 + 7) % 7

month_name = months[month - 1]
ordinal = day_i + endings[day - 1]

x_name = week[x]

print '----------------------------------------'
print month_name + ' ' + ordinal + ', ' + year_i
print x_name + '\n'
raw_input("Press <Enter>")
