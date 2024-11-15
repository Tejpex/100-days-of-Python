import smtplib
import datetime as dt
import random

my_email = "email"
my_password = "password"

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)

if weekday == 1:
    with smtplib.SMTP("address", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                           to_addrs="email@mail.com",
                           msg=f"Subject:Quote of the day \n\nHi there! \n{quote}"
                           )
else:
    print(weekday)

# specific_date = dt.datetime(year=1980, month=10, day=15)
