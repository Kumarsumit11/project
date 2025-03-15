import datetime

def get_day_of_week(year, month, day):
    # Create a date object using the datetime module
    date = datetime.date(year, month, day)
    
    day_name = date.strftime("%A")  # %A gives the full weekday name (e.g., Monday, Tuesday)
    
    return day_name

year = int(input("Enter the year (e.g., 2023): "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

day_of_week = get_day_of_week(year, month, day)

print(f"The day of the week for {month}/{day}/{year} is {day_of_week}.")
