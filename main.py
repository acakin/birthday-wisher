import datetime as dt
import random
import smtplib
import pandas as pd

data = pd.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
now = dt.datetime.now()
month = now.month
day = now.day
email1 = "qwe@gmail.com"
password1 = "***"

for _ in birthday_dict:
    if _["month"] == month and _["day"] == day:
        name = _["name"]

        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt",
                  encoding="ascii", errors="ignore") as letter_file:
            birthday_letter = letter_file.read()
            birthday_letter = birthday_letter.replace("[NAME]", name)
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=email1, password=password1)
                connection.sendmail(from_addr=email1, to_addrs=_["email"],
                                    msg=f"Subject:Happy birthday\n\n{birthday_letter}")
