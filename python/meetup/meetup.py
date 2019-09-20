import datetime
from calendar import monthrange


class MeetupDayException:
    pass


def meetup(year, month, week, day_of_week):

    weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    if week == 'teenth':
        day = [d for d in range(13, 20)
               if datetime.date(year, month, d).weekday() == weekdays[day_of_week]][0]
    else:
        last_day = monthrange(year, month)[1]
        list_of_dates = [day for day in range(1, last_day + 1)
                         if datetime.date(year, month, day).weekday() == weekdays[day_of_week]]
        if week == 'last':
            day = list_of_dates[-1]
        else:
            try:
                day = list_of_dates[int(week[0]) - 1]
            except IndexError:
                raise MeetupDayException

    return datetime.date(year, month, day)
