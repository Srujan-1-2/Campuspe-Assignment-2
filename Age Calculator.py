from datetime import date
year = int(input("Enter your birth year (e.g., 2006): "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))
birth_date = date(year, month, day)
today = date.today()
age_years = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age_years -= 1
age_months = today.month - birth_date.month
if today.day < birth_date.day:
    age_months -= 1
age_months %= 12
if today.day >= birth_date.day:
    age_days = today.day - birth_date.day
else:
    last_month = today.month - 1 if today.month > 1 else 12
    year_of_last_month = today.year if today.month > 1 else today.year - 1
    from calendar import monthrange
    days_in_last_month = monthrange(year_of_last_month, last_month)[1]
    age_days = today.day + (days_in_last_month - birth_date.day)
print(f"\nYou are {age_years} years, {age_months} months, and {age_days} days old.")