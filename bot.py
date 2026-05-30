import logging
import requests

# Configuration
TOKEN = "8489873384:AAFB7nC0DcCBJNF_nQNj3a_vWJui7thcO0g"
CHAT_ID = "-5117149177"

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_telegram_message(message_text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message_text,
        "parse_mode": "Markdown"  # Optional: For message formatting
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Check for HTTP errors
        logging.info("Message sent successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send message: {e}")

# Example of usage
sample_message = "New job received! *Job Name*: Project X. *Type*: Freelance"
send_telegram_message(sample_message)
