import smtplib
import pandas as pd
from datetime import datetime
import random

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "your-email@gmail.com"
GMAIL_PASSWORD = "your-email-password"

def send_email(to_address, subject, message):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(GMAIL_USER, to_address, email_message)
        print(f"Successfully sent email to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")
        

def send_quotes():
    today = datetime.today()
    print(f"Today is: {today.strftime('%A')}")
    
    if today.weekday() == 0: 
        try:
            quotes = pd.read_csv("quotes.csv")
        except FileNotFoundError:
            print("Error: quotes.csv not found.")
            return
        
        try:
            emails = pd.read_csv("emails.csv")
        except FileNotFoundError:
            print("Error: emails.csv not found.")
            return
        
        quote = random.choice(quotes["quote"])
        
        for index, row in emails.iterrows():
            name = row["name"]
            email = row["email"]
            subject = "*** Is Hafte ke Motivational Shayari ***"
            message = f"Hi {name},\nYeh hai aapke is hafte ke motivational Shayari ->\n{quote}"
            send_email(email, subject, message)
    else:
        print("Not Monday. Not sending quotes.")

if __name__ == "__main__":
    send_quotes()

