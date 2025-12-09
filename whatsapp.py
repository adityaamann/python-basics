# step 1: Install the Twilio library
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step 2: Set up your Twilio credentials
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

# step 3: Define the message details
def send_whatsapp_message(rec_number, message_body):
    try:
        message = client.messages.create(
            from_= '',
            body = message_body,
            to = f'whatsapp:{rec_number}'
        )
        print(f"Message sent to {rec_number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {rec_number}: {e}")


#step 4: Schedule messages
name = input("Enter your name: ")
rec_number = input("Enter recipient WhatsApp number (with country code, e.g., +1234567890): ")
message_body = f"Hello, this is a scheduled message from {name}."   

# Set the time to send the message (24-hour format)
date_str = input("Enter the date to send the message (YYYY-MM_DD): ")
time_str = input("Enter the time to send the message(HH:MM, 24-hour format): ")

#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
current_datetime = datetime.now()

#calculate time difference
time_difference = (schedule_datetime - current_datetime).total_seconds()

if time_difference <= 0:
    print("The scheduled time is in the past. Please enter a future time.")
else:
    print(f"Message scheduled to be sent at {schedule_datetime}.")

    #wait until the scheduled time
    time.sleep(time_difference)
    send_whatsapp_message(rec_number, message_body)
