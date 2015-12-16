from datetime import date
import calendar


def meetup_day(year, month, day, week):
    days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
            'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    day_of_month = [d for d in calendar.Calendar().itermonthdates(year, month) if d.weekday() == days[day] and d.month == month]

    if week == '1st':
        return day_of_month[0]

    elif week == 'last':
        return day_of_month[-1]

    elif week == '2nd':
        return day_of_month[1]

    elif week == '3rd':
        return day_of_month[2]

    elif week == 'teenth':
        return day_of_month[2]



    # for i in range(date_ranges[week][0], date_ranges[week][1]):
    #     if (date(year, month, i).weekday()) == days[day]:
    #         return date(year, month, i)


