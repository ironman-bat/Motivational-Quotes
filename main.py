import smtplib
import datetime as dt
import random

MY_EMAIL = "PLACE YOUR EMAIL HERE
MY_PASSWORD = "PLACE YOUR APP PASSWORD HERE"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )











# import smtplib
#
# my_email = "PLACE YOUR EMAIL HERE"
# password = "PLACE YOUR APP PASSWORD HERE"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="PLACE YOUR EMAIL HERE",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=YOUR YEAR, month=YOUR MONTH, day=YOUR DAY, hour=YOUR HOUR)
# print(date_of_birth)
