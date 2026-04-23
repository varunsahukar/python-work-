"""
Topic 13: Working with Dates and Times
======================================
Covers: datetime.now, creating datetime objects, formatting, time deltas
"""
from datetime import datetime, timedelta

# ─────────────────────────────────────────
# 1. Getting the Current Date and Time
# ─────────────────────────────────────────
now = datetime.now()
print(f"Current date and time: {now}")

today = datetime.now().date()
print(f"Today's date: {today}")

# ─────────────────────────────────────────
# 2. Creating Specific Datetime Objects
# ─────────────────────────────────────────
specific_date = datetime(2023, 10, 27, 10, 30, 0)
print(f"Specific date: {specific_date}")

# ─────────────────────────────────────────
# 3. Formatting Dates and Times (strftime)
# ─────────────────────────────────────────
# %Y - Year (e.g., 2023)
# %m - Month (01-12)
# %d - Day (01-31)
# %H - Hour (00-23)
# %M - Minute (00-59)
# %S - Second (00-59)
# %A - Weekday (e.g., Friday)
# %B - Month Name (e.g., October)

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")

pretty_date = now.strftime("Today is %A, %B %d, %Y")
print(f"Pretty date: {pretty_date}")

# ─────────────────────────────────────────
# 4. Parsing Dates and Times (strptime)
# ─────────────────────────────────────────
date_string = "2023-10-27 12:00:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed date: {parsed_date}")

# ─────────────────────────────────────────
# 5. Time Deltas: Calculating differences
# ─────────────────────────────────────────
one_day = timedelta(days=1)
yesterday = now - one_day
print(f"Yesterday was: {yesterday}")

two_weeks = timedelta(weeks=2)
in_two_weeks = now + two_weeks
print(f"In two weeks it will be: {in_two_weeks}")

# Calculate the difference between two dates
date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 12, 31)
difference = date2 - date1
print(f"Difference between dates: {difference.days} days")