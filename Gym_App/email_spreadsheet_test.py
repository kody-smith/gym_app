import pandas as pd
import smtplib, ssl
from email.mime.text import MIMEText
from email.header import Header
from datetime import date
import user_info



# No attachements, just simple plain-text or html content
def send_simple_email(host, subject, from_addr, to_addr, body, password):
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


if __name__ == "__main__":
    today = date.today()

    # Textual month, day and year	
    curr_date = today.strftime("%B %d, %Y")
    
    # Reading excel content
    xls = pd.ExcelFile("Workout Program - Kody Smith.xlsx")
    df = pd.read_excel(xls, 'Legs 1')

    # Editing Email Info
    host = "smtp.gmail.com"     # Using Gmail server to send the email
    subject = f"Workout Plan: {curr_date}"
    html_body = f"""<h1> Todays Workout Plan </h1> {df.to_html()}"""
    from_addr, to_addr = "krsmith1999@gmail.com", "krsmith1999@gmail.com"

    # Sending Email
    send_simple_email(host, subject, from_addr, to_addr, html_body, user_info.password)
