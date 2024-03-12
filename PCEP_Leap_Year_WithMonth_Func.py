def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if year < 1582:
        print("Not within the Gregorian calendar period (after 1582)")
        return None
    else:
        if year % 4 != 0:
            #NEM OSZTHATÓ 4el
            return False
        elif year % 100 != 0:
            #NEM OSZTHATÓ 100al
            return True
        elif year % 400 != 0:
            #NEM OSZTHATÓ 400al
            return False
        else:
            return True

def days_in_month(year, month):
#
# Write your new code here.
#
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
    if (is_year_leap(year)):
        months[2] = 29
        return months[month]
    else:
        return months[month]
    
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")