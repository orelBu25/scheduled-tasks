# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.



import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
import random

NUM_OF_TEMPLATES = 3

def send_greetings(name, mail):
    letter_template = random.randint(1,NUM_OF_TEMPLATES)
    with open(f"letter_templates/letter_{letter_template}.txt") as template:
        content = template.read().replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=mail,msg=f"Subject:Happy Birthday!\n\n{content}")




now = dt.datetime.now()
with open("birthdays.csv") as birthdays:
    data = pd.read_csv(birthdays)
    for index, row in data.iterrows():
        if row["month"] == now.month and row["day"] == now.day:
            send_greetings(row["name"], row["email"])




