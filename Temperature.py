Temperature_1 = 23.87654321
Temperature_2 = 23.8760
Temperature_3 = 23.8769

reading_1 = round(Temperature_1,3)
reading_2 = round(Temperature_2,3)
reading_3 = round(Temperature_3,3)


reading_average = (reading_1+reading_2+reading_3)/3
average = (Temperature_1+Temperature_2+Temperature_3)/3

diff =reading_average - average

print(f"Rounded Temperature 1: {reading_1}°C")
print(f"Rounded Temperature 2: {reading_2}°C")
print(f"Rounded Temperature 3: {reading_3}°C")
print(f"Average Temperature: {reading_average}°C")
print(f"Difference in Average Temperature: {diff}°C")
