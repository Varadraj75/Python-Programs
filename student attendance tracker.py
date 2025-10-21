# Student attendance tracker

name = input("Enter the name").strip()
total_days = int(input("Enter the days"))

day = 1

while day<=total_days:
    if day ==3:
        day += 1
        continue
    else:
        print(f"Attendance recorded for {name} on day {day}")
        day += 1



