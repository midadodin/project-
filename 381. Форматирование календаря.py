from math import ceil

nDays, weekday = input().split()
nDays = int(nDays)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

start_day = 0
for i in range(7):
    if weekdays[i] == weekday:
        start_day = i
        break

def format_digit(n):
    if n < 10:
        return '.' + str(n)
    else:
        return str(n)
    
n_weeks = ceil((nDays + start_day) / 7)
current_date = 1

for i in range(7):
    end = ' ' if i < 6 else '\n'
    if i < start_day:
        print('..', end=end)
    else:
        print(format_digit(current_date), end=end)
        current_date += 1

for i in range(n_weeks - 1):
    for j in range(7):
        if current_date > nDays:
            break
        end = ' ' if j < 6 else '\n'
        print(format_digit(current_date), end=end)
        current_date += 1