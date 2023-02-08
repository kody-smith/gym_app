import schedule
import time
import pandas as pd
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import user_info
import send
from datetime import datetime

def mail():
    today = datetime.today()

    # Textual month, day and year	
    curr_date = today.strftime("%B %d, %Y")
    
    # Reading excel content
    xls = pd.ExcelFile("Workout Program - Kody Smith.xlsx")
    df = pd.read_excel(xls, 'Active Rest')

    # Editing Email Info
    recipient_list = ["krsmith1999@gmail.com","Christian.T.Schafer@gmail.com"]
    host = "smtp.gmail.com"     # Using Gmail server to send the email
    subject = f"Workout Plan: {curr_date}"
    html_body = f"""<h1> Todays Workout Plan </h1> {df.to_html()}"""
    for recipient in recipient_list:
        from_addr, to_addr = "krsmith1999@gmail.com", recipient
        # Sending Email
        send.send_email(host, subject, from_addr, to_addr, html_body, user_info.fernet.decrypt(user_info.password).decode())


if __name__ == "__main__":
    # schedule.every(2).seconds.do(mail)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    mail()