import datetime

date = input()
week = datetime.date(2024,7,3).weekday()

week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print(week_days[week])