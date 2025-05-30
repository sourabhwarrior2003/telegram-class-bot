import requests

# Replace with your actual bot token and chat ID
TOKEN = "7925848334:AAGCdfQqSKj2KDgQ-zlCo2yJ9xSf1JNMCLA"
CHAT_ID = "1694959583"
MESSAGE = "📢 Hello classs Your class has been moved to 4 PM."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": MESSAGE
}

res = requests.post(url, data=payload)
print("Message status:", res.status_code)
