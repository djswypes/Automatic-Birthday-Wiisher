##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib

MY_EMAIL = 'testpython107@gmail.com'
MY_PASSWORD = '1234!@#$'

today = dt.datetime.now()
month = today.month
day = today.day
data = pandas.read_csv('birthdays.csv')

birthday_today = data[(data.month == month) & (data.day == day)].to_dict(orient='records')
birthday_names = []
birthday_emails = []
for birthday in birthday_today:
    birthday_names.append(birthday['name'])
    birthday_emails.append(birthday['email'])
for index in range(len(birthday_names)):
    letter_choice = random.randint(1, 3)
    with open(f'letter_templates/letter_{letter_choice}.txt') as file:
        message = file.read()
        message = message.replace('[NAME]', birthday_names[index])
        print(message)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            to_addrs=birthday_emails[index],
            from_addr=MY_EMAIL,
            msg=f'Subject:Happy Birthday\n\n{message}'
        )
