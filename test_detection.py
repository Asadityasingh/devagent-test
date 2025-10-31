"""DevAgent Swarm Detection Test - Safe Version"""

def login_user(username, password):
    """SQL injection vulnerability example"""
    query = "SELECT * FROM users WHERE user = '" + username + "'"
    return db.execute(query)

def send_email(recipient):
    """Hardcoded credential example"""
    api_token = "test_api_token_12345_FAKE"  # No sk_ prefix
    mail_password = "TestMailPass123"
    return f"Sending to {recipient}"

# Test credentials for detection
DB_CONNECTION = "postgresql://testuser:TestPass123@localhost/testdb"


def calculate_price(price):
    """Division by zero risk"""
    tax = get_tax()  # May return 0
    return price / tax

def read_config(path):
    """Path traversal risk"""
    return open(path).read()
