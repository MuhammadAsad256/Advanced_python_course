import requests
import smtplib
from datetime import datetime
import json


SHEETY_ENDPOINT = "https://spreadsheets.google.com"


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "your-email@example.com"
GMAIL_PASSWORD = "Password"

def fetch_data_from_sheety():
    response = requests.get(url=SHEETY_ENDPOINT)
    data = response.json()
    return data["sheet1"]

# print(fetch_data_from_sheety())
def analyze_trends(data):
    current_season = get_current_season()
    return [trend for trend in data if trend.get('season') == current_season]

# Function to get the current season
def get_current_season():
    current_month = datetime.now().month
    if current_month in [12, 1, 2]:
        return "Winter"
    elif current_month in [3, 4, 5]:
        return "Spring"
    elif current_month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

def create_email_template(trend):
    subject = f"{trend['season']} is here! New arrivals and special offers:"
    message = f"{trend['season']} is here! Check out our new arrivals and special offers: {', '.join([product['name'] for product in json.loads(trend['products'])])},\nThis is link of product to buy easy: {', '.join([product['link'] for product in json.loads(trend['products'])])}"
    return subject, message

def send_email(to_address, subject, message):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, to_address, f"Subject: {subject}\n\n{message}")
        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def main():
    data = fetch_data_from_sheety()
    trends = analyze_trends(data)
    for trend in trends:
        subject, message = create_email_template(trend)
        customers = json.loads(trend['customers'])
        for customer in customers:
            send_email(customer['email'], subject, message)

if __name__ == "__main__":
    main()
