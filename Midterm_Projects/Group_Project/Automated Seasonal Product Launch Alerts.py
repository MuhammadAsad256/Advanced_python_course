import pandas as pd
import requests
import smtplib

# Sheety endpoint URL
SHEETY_ENDPOINT = "sheety url"
# Gmail SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = ""
GMAIL_PASSWORD = ""

def fetch_data_from_sheety():
    """Fetch data from Sheety"""
    response = requests.get(url=SHEETY_ENDPOINT)
    data = response.json()
    return data

def analyze_trends(data):
    """Analyze seasonal trends"""
    trends = []
    for row in data:
        trend = row['trend']
        if trend not in trends:
            trends.append(trend)
    return trends

def create_email_template(trend, product_name, product_description, product_link):
    """Create a customized email template"""
    subject = f"New Arrival: {product_name} for {trend}!"
    message = f"""
Hi there,

We're excited to introduce our new arrival for {trend}: {product_name}!

{product_description}

Get it now: {product_link}

Best,
[Your Name]
"""
    return subject, message

def send_email(to_address, subject, message):
    """Send email using Gmail SMTP"""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(GMAIL_USER, to_address, email_message)
        print(f"Successfully sent email to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def main():
    data = fetch_data_from_sheety()
    trends = analyze_trends(data)
    for trend in trends:
        for row in data:
            if row["trend"] == trend:
                product_name = row["product_name"]
                product_description = row["product_description"]
                product_link = row["product_link"]
                email_subject, email_message = create_email_template(trend, product_name, product_description, product_link)
                send_email(row["email"], email_subject, email_message)

if __name__ == "__main__":
    main()
