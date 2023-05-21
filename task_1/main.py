import smtplib
import os
import schedule
import time
import datetime
import json
import config
import mysql.connector
from email.mime.text import MIMEText
from DB.database import work_with_db
from DB.sql_provider import SQL_Provider
from message.send_email import SendEmail


def main():
    email_sender = SendEmail()
    email_sender.run()


if __name__ == "__main__":
    main()


