year = int(input("Enter a year: "))
leap_year = False

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        #NEM OSZTHATÓ 4el
        leap_year = False
    elif year % 100 != 0:
        #NEM OSZTHATÓ 100al
        leap_year = True
    elif year % 400 != 0:
        #NEM OSZTHATÓ 400al
        leap_year = False
    else:
        leap_year = True
            
    if leap_year:
        print("LEAP YEAR")
    else:
        print("COMMON YEAR")