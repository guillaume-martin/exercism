import datetime
import calendar


class MeetupDayException:
    pass


def meetup(year, month, week, day_of_week):
    cal = calendar.Calendar()
    weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    month_days = cal.itermonthdays2(year, month)
    days = [day for day, weekday in month_days if weekday == weekdays[day_of_week] and day > 0]

    try:
        if week == 'teenth':
            day = [d for d in days if d in range(13, 20)][0]
        elif week == 'last':
            day = days[-1]
        else:
            day = days[int(week[0]) - 1]
    except Exception:
        raise MeetupDayException

    return datetime.date(year, month, day)
