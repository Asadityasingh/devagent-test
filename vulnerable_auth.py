def authenticate_user(username, password):
    # Vulnerable: Direct SQL injection
    sql_query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    # Simulate: cursor.execute(sql_query)
    return True

# Vulnerable: Hardcoded secret
API_SECRET = "sk-1234567890-super-secret-key"

def get_api_key():
    return API_SECRET
