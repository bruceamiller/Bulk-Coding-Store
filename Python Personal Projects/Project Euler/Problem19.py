def getMonthLengths(year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and not year % 100 == 0:
        months[1] += 1
    elif year % 400 == 0:
        months[1] += 1
    return months

sundaysFirstMonth = 0
daysTillSunday = 6 #December 31, 1900 is a monday, 6 days from sunday
for year in range(1901, 2001):
    months = getMonthLengths(year)
    print(year, months)
    for m in months:
        if daysTillSunday == 1:
            sundaysFirstMonth += 1
        print(daysTillSunday, m % 7)
        daysTillSunday -= m % 7
        if daysTillSunday < 1:
            daysTillSunday += 7

print(sundaysFirstMonth)