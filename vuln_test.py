def user_login(user_id):
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return db.execute(query)

def get_api_key():
    # Hardcoded secret
    return "sk-1234567890abcdef1234567890abcdef"
