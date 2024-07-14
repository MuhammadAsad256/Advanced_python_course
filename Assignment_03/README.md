# Weekly Motivational Quotes Sender

This Python script sends motivational quotes via email every Monday. It reads quotes and recipient email addresses from CSV files and sends an email with a random quote to each recipient.

## Features

- **Send Motivational Quotes**: Sends a randomly selected motivational quote to each recipient.
- **Weekly Schedule**: Only sends emails on Mondays.
- **Customizable Email Settings**: Configurable Gmail SMTP server settings.

## Requirements

- Python 3.x
- `pandas` library
- Access to a Gmail account (for sending emails)

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/weekly-motivational-quotes-sender.git
   cd weekly-motivational-quotes-sender
2. **Install Dependencies**
 - Make sure you have the required libraries installed. You can use pip to install them:
3. **Configure Email Settings**
 - Open the script and update the GMAIL_USER and GMAIL_PASSWORD variables with your Gmail account details.
4. **Prepare CSV Files**
- 'quotes.csv': Contains a column `quote`' with motivational quotes.
- 'emails.csv': Contains columns `name`' and `email` for recipients.
5. **Run the Script**
  - ***python your_script_name.py***
## Troubleshooting
- Ensure "Allow less secure apps" is enabled on your Gmail account or use an app password if 2-step verification is enabled.
- Make sure `quotes.csv` and `emails.csv` are in the same directory as the script.
