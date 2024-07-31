
# Student Absence Notification System

This Python script is designed to notify students about their absence from class and provide a way to inform the administration about their absence. The script uses a Google Sheet as the data source and Gmail's SMTP server to send notifications.

## Features

- **Fetch Student Data:** Retrieves student attendance data from a Google Sheet via the Sheety API.
- **Identify Absences:** Checks the attendance status for each student and identifies those who were absent.
- **Send Notifications:** Sends an email notification to the absent students informing them about their absence and requesting an explanation.
- **Email Configuration:** Utilizes Gmail’s SMTP server for sending emails.
- **Day Check:** Only performs attendance checks and sends notifications on weekdays (Monday through Friday).

## Requirements

- Python 3.x
- `requests` library for making HTTP requests.
- `smtplib` for sending emails.
- `pandas` for data manipulation (though it is imported but not used in the provided script).

## Setup
1. **Google Sheet Setup:**
   - Replace 'SHEETY_ENDPOINT' with the unique API link to your Google Sheet.
2. **Gmail Configuration:**
   - Replace `GMAIL_USER` and `GMAIL_PASSWORD` with your Gmail credentials.
3. **Script Execution:**
   - Run the script in a Python environment. Ensure you have an internet connection for fetching data and sending emails.
## Usage
1. **Update the API Link:**
   - Modify the 'SHEETY_ENDPOINT' variable with your Google Sheet API endpoint.
2. **Email Credentials:**
   - Set your Gmail email address and password in the script.
3. **Execute the Script:**
   - Run the script to fetch attendance data, identify absences, and send email notifications.

## Security Note
- Ensure you handle your Gmail credentials securely. Consider using environment variables or a secure credential store to manage sensitive information.
