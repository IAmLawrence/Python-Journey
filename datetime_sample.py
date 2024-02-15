import datetime

print(dir(datetime))

date_and_time_now = datetime.datetime.now()
print("Date and time: ", date_and_time_now)

date_today = datetime.date.today()
print("Date: ", date_today)

sample_date = datetime.date(2016, 12, 30)
print("Sample Date: ", sample_date)

timestamp = datetime.date.fromtimestamp(2)
print("timestamp: ", timestamp)

unix_timestamps = [1609459200, 1612137600, 1614556800]  # List of Unix timestamps
for timestamp in unix_timestamps:
    date_time = datetime.datetime.fromtimestamp(timestamp)
    print("Logged Time:", date_time)

filtered_dates = [datetime.datetime.fromtimestamp(ts) for ts in unix_timestamps if ts > 1609459200]

print("Filtered Dates:", filtered_dates)

sample_set_of_time = datetime.time(8, 24, 1)
print("Sample time:", sample_set_of_time)
print("Hour only: ", sample_set_of_time.hour)
print("Minute only: ", sample_set_of_time.minute)
print("Second only: ", sample_set_of_time.second)

my_birth_date = datetime.date(year=1997, month=4, day=2)
date_ngayon = datetime.date.today()
exist_days = date_ngayon - my_birth_date
print("My Birthdate: ", my_birth_date)
print("Date Ngayon: ", date_ngayon)
print("My total days of existence: ", exist_days)

date_timedelta1 = datetime.timedelta(weeks=2, days=10, hours=3)
date_timedelta2 = datetime.timedelta(weeks=1, days=5, hours=2)
total_date_timedelta = date_timedelta1 - date_timedelta2
print("total timedelta: ", total_date_timedelta)
print("total seconds: ", total_date_timedelta.total_seconds())

str_date = date_ngayon.strftime("%m/%d/%Y")
print("String Date: ", str_date)
print("String Date type: ", type(str_date))
string_date = "April 2,2020"
converted_str_date = datetime.datetime.strptime(string_date, "%B %d,%Y")
print("From Str to Date: ", converted_str_date)
print("converted_str_date type: ", type(converted_str_date))