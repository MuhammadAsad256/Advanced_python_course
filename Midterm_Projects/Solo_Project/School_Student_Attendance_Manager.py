import requests
import smtplib
from datetime import datetime
import pandas as pd

SHEETY_ENDPOINT = "https://api.sheety.co/your-unique-api-link"

response = requests.get(url=SHEETY_ENDPOINT)
data = response.json()

all_students = data["Sheet_Name"]

absent_students = []
for student in all_students:
    if student['attendance']!= "P":
        absent_students.append(student)
    else:
        print(f"Today {student['student']} are present")

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
        print(f"We have informed {student['student']} of their absence via email")
        print(f"A confirmation email has also been sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

for student in absent_students:
    subject = "Absence Notification"
    message = f"Hello {student['student']}, you were absent today. Please let us know the reason for your absence."
    send_email(student['email'], subject, message)