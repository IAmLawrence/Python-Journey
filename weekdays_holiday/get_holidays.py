from datetime import timedelta, datetime
import pandas as pd
from holidays import country_holidays


def get_current_yr_holidays(country, years):
    ph_holidays = country_holidays(country=country, years=years)

    print("ph_holidays>", ph_holidays)
    return ph_holidays


def get_holidays(country, years):
    current_holidays = []
    for hol in get_current_yr_holidays(country, years).items():
        current_holidays.append(hol[0].strftime('%Y-%m-%d'))

    return current_holidays


input_country = input("Please enter country: ")
input_year = int(input("Please enter Year: "))


def vals_to_append(date, day, **additional_data):
    vals = {
        'Date': date,
        'Day': day,
    }

    vals.update(additional_data)

    return vals


def generate_weekdays(start_date, end_date, holidays):
    start_date = start_date
    weekdays = []

    while start_date <= end_date:
        if start_date.weekday() < 5 and start_date.strftime('%Y-%m-%d') not in holidays:

            weekdays.append(
                vals_to_append(start_date.strftime('%Y-%m-%d'), start_date.strftime('%A'))
            )

        start_date += timedelta(days=1)

    return weekdays


start_date_str = input("Please Enter Start date with this format: year-month-day (2024-1-1)")
end_date_str = input("Please Enter End date with this format: year-month-day (2024-12-31)")
try:
    start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')

    df = pd.DataFrame(generate_weekdays(start_date_obj, end_date_obj, get_holidays(input_country, input_year)))

    excel_filename = 'weekdays_excluding_holidays.xlsx'
    df.to_excel(excel_filename, index=False)

    print(f"Generated weekdays saved to '{excel_filename}'.")

except ValueError:
    print("Invalid date format. Please enter the date in the format: year-month-day (e.g., 2024-01-01)")






