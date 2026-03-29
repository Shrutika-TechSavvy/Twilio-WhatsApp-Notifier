from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get credentials from .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

# Send WhatsApp template message
message = client.messages.create(
    from_=os.getenv("TWILIO_WHATSAPP_NUMBER"),
    content_sid=os.getenv("TWILIO_CONTENT_SID"),
    content_variables='{"1":"12/1","2":"3pm"}', 
    to=os.getenv("MY_PHONE_NUMBER") # your number
)

print("Message SID:", message.sid)