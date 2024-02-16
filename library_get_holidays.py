from holidays import country_holidays

ph_holidays = country_holidays('PH', years=2024)
new_holidays = []
days_to = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in ph_holidays.items():
    print("day", day, type(day[0]), day[0].isoweekday())

    vals = ({
        'date': day[0],
        'day': days_to[day[0].isoweekday()-1],
        'events': day[1]
    })

    new_holidays.append(vals)
print('new_holidays>', new_holidays)

