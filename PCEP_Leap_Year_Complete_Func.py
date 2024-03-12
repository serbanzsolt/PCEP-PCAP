months = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11: 30,
    12 : 31
}

def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorian calendar period (after 1582)")
        return None
    else:
        if year % 4 != 0:
            #CANNOT DIVIDE WITH 4
            return False
        elif year % 100 != 0:
            #CANNOT DIVIDE WITH 100
            return True
        elif year % 400 != 0:
            #CANNOT DIVIDE WITH 400
            return False
        else:
            return True
        
def days_in_month(year, month):

    # LEAP YEAR'S FEBRUARY IS 29 DAY
    if (is_year_leap(year)):
        months[2] = 29
        return months[month]
    else:
        return months[month]

def day_of_year(year, month, day):
    if (is_year_leap(year)):
        return sum(months.values()) + 1
    else:
        return sum(months.values())

print(day_of_year(2000, 12, 31))
print(day_of_year(2024, 3, 12))
print(day_of_year(2001, 1, 1))
# totalofdays = sum(months.values())
# print(totalofdays)