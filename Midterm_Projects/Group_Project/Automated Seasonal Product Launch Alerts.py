
# Column Name	Description
# trend	:Seasonal trend (e.g., summer fashion, holiday season)
# product_name :	Name of the product
# product_description	: Brief description of the product
# product_link :	Link to the product page
# special_offer	: Special offer or discount (if applicable)
# email_subject	: Subject line for the email alert
# email_message :	Message body for the email alert

# Create a Sheety endpoint for your Google Sheet:

# Go to Sheety and create a new project.
# Connect your Google Sheet to Sheety.
# Get the Sheety endpoint URL (e.g., https://api.sheety.co/your_project_name/sheet_name).




    
# import pandas as pd
# import requests
# import smtplib

# # Sheety endpoint URL
# SHEETY_ENDPOINT = "https://api.sheety.co/dc6cc07e5d1ffdd8032e9ef02d0034cc/sheet1/sheet1"

# # Gmail SMTP settings
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587
# GMAIL_USER = "asadm2839@gmail.com"
# GMAIL_PASSWORD = "gqoo ptee niva oepx"

# def fetch_data_from_sheety():
#     """Fetch data from Sheety"""
#     response = requests.get(url=SHEETY_ENDPOINT)
#     data = response.json()
#     return data

# def analyze_trends(data):
#     """Analyze seasonal trends"""
#     trends = []
#     for row in data:
#         trend = row['trend']
#         if trend not in trends:
#             trends.append(trend)
#     return trends

# def create_email_template(trend, product_name, product_description, product_link):
#     """Create a customized email template"""
#     subject = f"New Arrival: {product_name} for {trend}!"
#     message = f"""
# Hi there,

# We're excited to introduce our new arrival for {trend}: {product_name}!

# {product_description}

# Get it now: {product_link}

# Best,
# [Your Name]
# """
#     return subject, message

# def send_email(to_address, subject, message):
#     """Send email using Gmail SMTP"""
#     try:
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             server.login(GMAIL_USER, GMAIL_PASSWORD)
#             email_message = f"Subject: {subject}\n\n{message}"
#             server.sendmail(GMAIL_USER, to_address, email_message)
#         print(f"Successfully sent email to {to_address}")
#     except Exception as e:
#         print(f"Failed to send email to {to_address}: {e}")

# def main():
#     data = fetch_data_from_sheety()
#     trends = analyze_trends(data)
#     for trend in trends:
#         for row in data:
#             if row["trend"] == trend:
#                 product_name = row["product_name"]
#                 product_description = row["product_description"]
#                 product_link = row["product_link"]
#                 email_subject, email_message = create_email_template(trend, product_name, product_description, product_link)
#                 send_email(row["email"], email_subject, email_message)

# if __name__ == "__main__":
#     main()














import os
import pandas as pd
import requests
import smtplib
from email.mime.text import MIMEText
from jinja2 import Template
from typing import Dict, List

# Load environment variables
SHEETY_ENDPOINT = os.getenv('ttps://api.sheety.co/dc6cc07e5d1ffdd8032e9ef02d0034cc/sheet1/sheet1')
GMAIL_USER = os.getenv('asadm2839@gmail.com')
GMAIL_PASSWORD = os.getenv('gqoo ptee niva oepx')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('587'))

def fetch_data_from_sheety() -> Dict[str, List[Dict[str, str]]]:
    """Fetch data from Sheety"""
    response = requests.get(url=SHEETY_ENDPOINT)
    data = response.json()
    return data

def analyze_trends(data: Dict[str, List[Dict[str, str]]]) -> List[str]:
    """Analyze seasonal trends"""
    trends = []
    for row in data['sheet1']:
        trend = row['trend']
        if trend not in trends:
            trends.append(trend)
    return trends

def create_email_template(
    trend: str,
    product_name: str,
    product_description: str,
    product_link: str
) -> str:
    """Create a customized email template"""
    template = Template("""
Hi there,

We're excited to introduce our new arrival for {{ trend }}: {{ product_name }}!

{{ product_description }}

Get it now: {{ product_link }}

Best,
[Your Name]
""")
    return template.render(trend=trend, product_name=product_name, product_description=product_description, product_link=product_link)

def send_email(to_address: str, subject: str, message: str) -> None:
    """Send email using Gmail SMTP"""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = MIMEText(message)
            email_message['Subject'] = subject
            server.sendmail(GMAIL_USER, to_address, email_message.as_string())
        print(f"Successfully sent email to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def main() -> None:
    data = fetch_data_from_sheety()
    trends = analyze_trends(data)
    for trend in trends:
        for row in data['sheet1']:
            if row["trend"] == trend:
                product_name = row["product_name"]
                product_description = row["product_description"]
                product_link = row["product_link"]
                email_subject = f"New Arrival: {product_name} for {trend}!"
                email_message = create_email_template(trend, product_name, product_description, product_link)
                send_email(row["email"], email_subject, email_message)

if __name__ == "__main__":

# import os
# import pandas as pd
# import requests
# import smtplib
# from email.mime.text import MIMEText
# from jinja2 import Template

# # Load environment variables
# SHEETY_ENDPOINT = os.environ['https://api.sheety.co/dc6cc07e5d1ffdd8032e9ef02d0034cc/sheet1/sheet1']
# GMAIL_USER = os.environ['asadm2839@gmail.com']
# GMAIL_PASSWORD = os.environ['gqoo ptee niva oepx']
# SMTP_SERVER = os.environ['smtp.gmail.com']
# SMTP_PORT = int(os.environ['587'])

# def fetch_data_from_sheety():
#     """Fetch data from Sheety"""
#     response = requests.get(url=SHEETY_ENDPOINT)
#     data = response.json()
#     return data

# def analyze_trends(data):
#     """Analyze seasonal trends"""
#     trends = []
#     for row in data:
#         trend = row['trend']
#         if trend not in trends:
#             trends.append(trend)
#     return trends

# def create_email_template(trend, product_name, product_description, product_link):
#     """Create a customized email template"""
#     template = Template("""
# Hi there,

# We're excited to introduce our new arrival for {{ trend }}: {{ product_name }}!

# {{ product_description }}

# Get it now: {{ product_link }}

# Best,
# [Your Name]
# """)
#     return template.render(trend=trend, product_name=product_name, product_description=product_description, product_link=product_link)

# def send_email(to_address, subject, message):
#     """Send email using Gmail SMTP"""
#     try:
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             server.login(GMAIL_USER, GMAIL_PASSWORD)
#             email_message = MIMEText(message)
#             email_message['Subject'] = subject
#             server.sendmail(GMAIL_USER, to_address, email_message.as_string())
#         print(f"Successfully sent email to {to_address}")
#     except Exception as e:
#         print(f"Failed to send email to {to_address}: {e}")

# def main():
#     data = fetch_data_from_sheety()
#     trends = analyze_trends(data)
#     for trend in trends:
#         for row in data:
#             if row["trend"] == trend:
#                 product_name = row["product_name"]
#                 product_description = row["product_description"]
#                 product_link = row["product_link"]
#                 email_subject = f"New Arrival: {product_name} for {trend}!"
#                 email_message = create_email_template(trend, product_name, product_description, product_link)
#                 send_email(row["email"], email_subject, email_message)

# if __name__ == "__main__":
    main()
