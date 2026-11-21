from datetime import datetime
event_title = input("Event Title: ")
year_ = input("Year: ")
month_ = input("Month: ")
day_ = input("Day: ")

date_string = f"{year_} {month_} {day_}"
event_date = datetime.strptime(date_string, "%Y %B %d")

print("Event:", event_title.title())
print("Date:", event_date.strftime("%B %d, %Y"))
print("Year:", f"{year_}")
print("Month:", f"{month_}")
print("Day:", f"{day_}")
print("Weekday:", event_date.strftime("%A"))

