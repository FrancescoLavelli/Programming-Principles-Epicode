"""***The .timetuple() method ***
in Python is a method available on `datetime` objects that returns a `time.struct_time` object, which is a named tuple representation of the date and time.

Here's an explanation of what it does:

1. It converts a `datetime` object into a `time.struct_time` object (similar to what `time.localtime()` returns)
2. The returned tuple contains the following attributes:
   - tm_year: Year (e.g., 2025)
   - tm_mon: Month (1-12)
   - tm_mday: Day of the month (1-31)
   - tm_hour: Hour (0-23)
   - tm_min: Minutes (0-59)
   - tm_sec: Seconds (0-59)
   - tm_wday: Day of the week (0-6, 0 is Monday)
   - tm_yday: Day of the year (1-366)
   - tm_isdst: Daylight Saving Time flag (1 if in effect, 0 if not, -1 if unknown)
"""

from datetime import datetime

# Create a datetime object
now = datetime.now()

# Get the time tuple
time_tuple = now.timetuple()

# Access elements of the tuple
print(f"Year: {time_tuple.tm_year}, Type: {type(time_tuple.tm_year)}")
print(f"Month: {time_tuple.tm_mon}")
print(f"Day: {time_tuple.tm_mday}")
print(f"Day of year: {time_tuple.tm_yday}")
