import calendar

date = input().split()
result_day = calendar.weekday(int(date[2]), int(date[0].strip('0')), int(date[1].strip('0')))

print([*calendar.day_name][result_day].upper())