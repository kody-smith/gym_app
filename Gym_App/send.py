'''Gym Tracker'''
'''Developer: Kody Smith'''
'''Computer Science Student @ BYU-I'''
'''Last Edit: October 15th, 2022'''



'''This app sends a user emails of workout plans by day with sets,reps,and weight'''


from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import os
import user_info
import pandas as pd
from datetime import datetime
import scheduling

# No attachements, just simple plain-text or html content
def send_email(host, subject, from_addr, to_addr, body, password):
    # Instantiate MIMEText object
    message = MIMEText(body, 'html', 'utf-8')
    message['From'], message['To'] = from_addr, to_addr
    message['Subject'] = Header(subject, "utf-8")
    message = message.as_string()   # Because SMTP.sendmail, required bytes-like string. Otherwise you will see error like: Error: expected string or bytes-like object

    try:
        import ssl
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(host, 465, context=context)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()
        print("Email Sent!")
    

