from datetime import date, datetime
today = date.today()

print(today)

# Methods for to extracting 'components' under different calendars
t = today.timetuple()
for i in t:
    print(i)
2002                # year
3                   # month
11                  # day
0
0
0
0                   # weekday (0 = Monday)
70                  # 70th day in the year
-1
print(f"Year: {t[0]}, Type: {type(t[0])}")
