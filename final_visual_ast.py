def calculate_price(base, tax):
    total = base + (base * tax)
    return total

def send_email(recipient, api_key):
    # Hardcoded API key
    return f"Sending to {recipient} with key {api_key}"

SECRET_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuv"
DATABASE_PASSWORD = "admin123"
