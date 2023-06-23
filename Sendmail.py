import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = '@outlook.com'
sender_password = ''
receiver_email = '@gmail.com'
subject = 'CSV File Attachment'
body = 'Hello,\n\nPlease find the attached CSV file.\n\nRegards,\nTest Email'

# Path to the CSV file
csv_path = 'C:/Users/Pawar/Desktop/projects/Fetch_data_from_sql_and_export_it_into_csv_and_send_it_on_mail/output.csv'

# Create a multipart message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Add the body content to the message
message.attach(MIMEText(body, 'plain'))

# Read the CSV file
with open(csv_path, 'rb') as file:
    # Attach the CSV file to the email
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(csv_path)}"')
    message.attach(attachment)

# Connect to the SMTP server and send the email
with smtplib.SMTP('smtp.office365.com', 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)

print('Email sent successfully.')
