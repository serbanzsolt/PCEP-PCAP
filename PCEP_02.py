hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

time_in_mins = mins + hour*60
newtime = time_in_mins + dura
result_hour = 0
if newtime / 60 > 24:
    result_hour = int((newtime / 60) % 24)
else:
    result_hour = int(newtime / 60)

result_min = newtime % 60

print(f"The end-time is: {result_hour}:{result_min}")

