import datetime


def gen_secs():
    for sec in range(0, 60):
        yield sec


def gen_minutes():
    for minute in range(0, 60):
        yield minute


def gen_hours():
    for hour in range(0, 24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for year in range(1, 13):
        yield year


def gen_days(month, leap_year=True):
    days_for_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year:
        days_for_month[2] = 29
    for day in range(1, days_for_month[month]+1):
        yield day


def gen_date():
    current_year = datetime.date.today().year
    count = 0
    for year in gen_years(current_year):
        for month in gen_months():
            for day in gen_days(month, is_leap_year(year)):
                for day_time in gen_time():
                    if count == 1000000:
                        year_time = "%02d/%02d/%04d" % (day, month, year)
                        print(year_time + " " + day_time)
                        count = 0
                        yield
                    count += 1


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    date_generator = gen_date()
    for i in range(0, 10):
        next(date_generator)
