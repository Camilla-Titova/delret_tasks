import smtplib
import os
import time
import schedule
import json
import config
import mysql.connector
from email.mime.text import MIMEText
from DB.database import work_with_db
from DB.sql_provider import SQL_Provider


class SendEmail:
    def __init__(self):
        self.interval = 10*60 # интервал в 10 мин
        self.count = 1

    """
    Метод check_table используется для извлечения информации из базы данных 
    и вызывает send_email для отправки email-уведомлений каждому пользователю из базы данных. 
    Каждому пользователю отправляется персональное сообщение с использованием его имени и фамилии. 
    
    Файл mke.sql содержит запрос на выборку информации о пользователях из базы данных.
    Файл db.json содержит конфигурационную информацию для подключения к базе данных.
    """
    def check_table(self):
        with open('configs/db.json', 'r') as f:
            dbconfig = json.load(f)
        print(f"Рассылка №{self.count}:")
        self.count += 1
        with open('sql/mke.sql', 'r') as f:
            sql_query = f.read()
        result = work_with_db(dbconfig, sql_query)
        for row in result:
            name = row["user_name"]
            lastname = row["user_lastname"]
            email = row["email"]
            message = f"Здравствуйте {name} {lastname}, это массовая рассылка.\nПросьба не отвечать на нее!!"
            print(self.send_email(email, message=message))

    """
    Метод send_email использует библиотеку smtplib для настройки SMTP-сервера 
    и отправки сообщения каждому пользователю в списке получателей.
    Он также использует библиотеку email.mime.text, 
    чтобы создать MIMEText объект с текстом сообщения и темой.
    
    sender - отправитель(ваш email)
    recipient - эл. почта получателя
    password - ваш пароль в почте/приложении
    """
    def send_email(self, email, message):
        sender = "your_email"
        recipient = email
        password = "your_password"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(sender, password)
            msg = MIMEText(message)
            msg["Subject"] = "МАССОВАЯ РАССЫЛКА!"
            server.sendmail(sender, recipient, msg.as_string())
            return "\tThe message was sent successfully!"
        except Exception as _ex:
            return f"{_ex}\nCheck your login or password please!"

    """
    Метод run использует модуль schedule для отложения отправки 
    email-уведомлений через заданный интервал времени, 
    затем запускает этот метод на бесконечном цикле с использованием while True.
    """
    def run(self):
        # определяет частоту отправки уведомлений
        schedule.every(self.interval).seconds.do(self.check_table)
        while True:
            schedule.run_pending()
            time.sleep(self.interval)
            if input("Quit? Y/N: ") == "Y":
                break
