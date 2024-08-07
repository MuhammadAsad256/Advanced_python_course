


import requests
import smtplib
from datetime import datetime
import json

# Sheety API endpoint
SHEETY_ENDPOINT = "https://api.sheety.co/dc6cc07e5d1ffdd8032e9ef02d0034cc/sheet1/sheet1"

# Gmail SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "asadm2839@gmail.com"
GMAIL_PASSWORD = "gumb plpe alji gumf"

# Function to fetch data from Sheety
def fetch_data_from_sheety():
    response = requests.get(url=SHEETY_ENDPOINT)
    data = response.json()
    return data["sheet1"]

# Function to analyze seasonal trends
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

# Function to create a stylish email template
def create_email_template(trend):
    subject = f"{trend['season']} is here! New arrivals and special offers:"
    
    products = json.loads(trend['products'])
    product_links = [f"<a href='{product['link']}' style='color: #f09f00; text-decoration: none;'>{product['name']}</a>" for product in products]
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{trend['season']} Product Launch</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h2 {{
                color: #333;
            }}
            p {{
                color: #555;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin: 10px 0;
            }}
            footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 0.9em;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>{trend['season']} is here!</h2>
            <p>Check out our new arrivals and special offers:</p>
            <ul>
                {''.join(f'<li>{link}</li>' for link in product_links)}
            </ul>
            <p>Happy shopping!</p>
            <footer>
                <p>&copy; 2024 Seasonal Product Launch. All rights reserved.</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return subject, html_content

# Function to send email using Gmail SMTP
def send_email(to_address, subject, message):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, to_address, f"Subject: {subject}\nContent-Type: text/html\n\n{message}")
        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

# Main function
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




