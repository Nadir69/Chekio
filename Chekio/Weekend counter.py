__author__ = 'v_shabalin'

from datetime import date, timedelta as td

def checkio(from_date, to_date):
    count = 0
    for day in range((to_date - from_date).days + 1):
        if (from_date + td(days=day)).isoweekday() > 5:
            count += 1
    return count


print checkio(date(2013, 2, 2), date(2013, 2, 3))