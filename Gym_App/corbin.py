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
    
    # initialize connection to our email server,
    # we will use gmail here
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
      
    # Login with your email and password
    smtp.login('krsmith1999@gmail.com', f'{user_info.fernet.decrypt(user_info.password).decode()}')
  
    # Call the message function
    msg = "You're Gay"
      
    # Make a list of emails, where you wanna send mail
    to = ["cjandrus99@gmail.com"]
  
    # Provide some data to the sendmail function!
    smtp.sendmail(from_addr="krsmith1999@gmail.com",
                  to_addrs=to, msg=msg.as_string())
      
    # Finally, don't forget to close the connection
    smtp.quit()  

if __name__ == "__main__":
    schedule.every().day.at("10:09").do(mail)

    while True:
        schedule.run_pending()
        time.sleep(1)