from datetime import date
import calendar


def meetup_day(year, month, day, week):
    days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
            'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    day_of_month = [d for d in calendar.Calendar().itermonthdates(
        year, month) if d.weekday() == days[day] and d.month == month]

    if week == 'teenth':
        teenth = filter(lambda x: x.day >= 13 and x.day <= 19, day_of_month)
        return teenth[0]

    elif week == 'last':
        return day_of_month[-1]

    else:
        return day_of_month[int(week[0]) - 1]
