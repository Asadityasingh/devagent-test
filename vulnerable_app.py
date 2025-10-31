from flask import Flask, request  # Assuming Flask for web context

app = Flask(__name__)

# Hardcoded secret - HIGH severity
API_SECRET_KEY = "sk-9876543210-super-vulnerable-key"

def get_db_connection():
    # Simulate DB
    return None

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # CRITICAL: SQL injection - direct string concat
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    # Simulate execution
    conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute(query)  # Vulnerable point
    
    if username == 'admin' and password == 'pass':  # Mock success
        return {'status': 'success', 'token': API_SECRET_KEY}
    return {'status': 'failed'}

@app.route('/api/data', methods=['GET'])
def get_data():
    # MEDIUM: No input validation on query param
    user_id = request.args.get('id')
    query = f"SELECT data FROM sensitive_table WHERE id={user_id}"  # Another injection risk
    
    # Simulate
    return {'data': f"User {user_id} info"}

if __name__ == '__main__':
    app.run(debug=True)
# Minor update for re-analysis
\n# Test sync trigger
\n# Re-trigger for fix
