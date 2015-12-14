from datetime import date
import calendar


def meetup_day(year, month, day, week):
    days = dict(zip(list(calendar.day_name), range(7)))
    date_ranges = {'teenth': [13, 19], '1st':[1, 8], '2nd': [8,15], '3rd': [15, 22],
        '4th':[22, 29], 'last':[25, 32], 'last_week_in_feb': [22,30]}

    if week == '5th':
        raise Exception("Please enter 'last' instead of '5th'")

    if month == 2 and week == 'last' and day == 'Sunday':
        week = 'last_week_in_feb'

    for i in range(date_ranges[week][0], date_ranges[week][1]):
        if (date(year, month, i).weekday()) == days[day]:
            return date(year, month, i)
