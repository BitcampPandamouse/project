from datetime import date, timedelta
start_date = date(2020, 1, 1)
end_date = date(2021, 1, 1)
delta = timedelta(days=7)
while start_date <= end_date:
    time = start_date.strftime("%Y-%m-%d")
    start_date += delta
    
    print(time)

