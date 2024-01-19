#  https://www.hackerrank.com/contests/projecteuler/challenges/euler019/
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def calculate_odd_days():
    odd_days = [0]
    od = 0

    for i in range(1, 400):
        if is_leap_year(i):
            od += 2
        else:
            od += 1
        od = od % 7
        odd_days.append(od)

    return odd_days

def day_has_sunday(date):
    odd_days = 0
    year, month, day = map(int, date.split())
    odd_days += day
    odd_days += months[month]

    if is_leap_year(year) and month > 2:
        odd_days += 1

    year = (year - 1) % 400
    odd_days += years[year]

    return odd_days % 7 == 0

months = {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
years = calculate_odd_days()

if __name__ == "__main__":
    for _ in range(int(input())):
        start_date = input().strip()
        end_date = input().strip()
        dates = []

        year, month, day = map(int, start_date.split())

        if day == 1:
            dates.append(f'{year} {month} {day}')

        day = 1
        e_year, e_month, e_day = map(int, end_date.split())

        while True:
            if month == 12:
                month = 0
                year += 1
            month += 1
            date = f"{year} {month} {day}"

            if year > e_year:
                break
            elif year == e_year:
                if month > e_month:
                    break
            dates.append(date)

        ans = sum(1 for date in dates if day_has_sunday(date))
        print(ans)
