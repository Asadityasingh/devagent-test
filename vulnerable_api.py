"""
Vulnerable API endpoints demonstrating multiple security issues
"""
from flask import Flask, request, session, render_template_string
import subprocess
import os
import sqlite3
import pickle
from functools import wraps
import requests

app = Flask(__name__)
app.secret_key = "hardcoded_secret_key_12345"  # ISSUE: Hardcoded secret

# Global database connection (resource leak)
db_connection = sqlite3.connect(":memory:")

# Cache without expiration (memory leak risk)
user_cache = {}
request_log = []

@app.route('/login', methods=['POST'])
def login():
    """ISSUE: Multiple security vulnerabilities here"""
    username = request.form.get('username')
    password = request.form.get('password')
    
    # ISSUE 1: SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = db_connection.execute(query)
    
    if result:
        session['user_id'] = result[0]['id']  # No session expiration
        return "Login successful"
    
    return "Login failed", 401


@app.route('/execute', methods=['POST'])
def execute_command():
    """ISSUE: Command injection vulnerability"""
    command = request.form.get('command')
    
    # ISSUE 2: Command injection - user input directly to shell
    output = subprocess.check_output(f"echo {command}", shell=True)
    
    return output


@app.route('/download', methods=['GET'])
def download_file():
    """ISSUE: Path traversal vulnerability"""
    filename = request.args.get('file')
    
    # ISSUE 3: Path traversal - no validation on user input
    filepath = f"/home/user/files/{filename}"
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    return content


@app.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ISSUE: Missing authentication check"""
    
    # ISSUE 4: No permission check - anyone can delete any user
    query = f"DELETE FROM users WHERE id={user_id}"
    db_connection.execute(query)
    db_connection.commit()
    
    return "User deleted"


@app.route('/search', methods=['GET'])
def search():
    """ISSUE: Multiple XSS vulnerabilities"""
    query = request.args.get('q')
    
    # ISSUE 5: XSS - unescaped user input in HTML
    html = f"<h1>Search results for: {query}</h1>"
    
    return render_template_string(html)


@app.route('/proxy', methods=['POST'])
def proxy_request():
    """ISSUE: SSRF and unvalidated redirects"""
    url = request.form.get('url')
    
    # ISSUE 6: Server-side request forgery - no URL validation
    response = requests.get(url, timeout=5)
    
    return response.text


@app.route('/upload', methods=['POST'])
def upload_file():
    """ISSUE: Unsafe file upload"""
    file = request.files['file']
    
    # ISSUE 7: No file validation - could upload malicious files
    filename = file.filename
    file.save(f"/tmp/{filename}")
    
    return "File uploaded"


@app.route('/cache', methods=['GET'])
def cache_data():
    """ISSUE: Memory leak - unbounded cache"""
    key = request.args.get('key')
    value = request.args.get('value')
    
    # ISSUE 8: Cache grows indefinitely - memory leak
    user_cache[key] = value
    request_log.append({'key': key, 'value': value, 'timestamp': str(os.urandom(32))})
    
    return f"Cached {key}"


@app.route('/process', methods=['POST'])
def process_data():
    """ISSUE: Unsafe deserialization"""
    data = request.form.get('data')
    
    # ISSUE 9: Pickle deserialization - arbitrary code execution
    try:
        obj = pickle.loads(data)  # Critical RCE vulnerability
        return str(obj)
    except Exception as e:
        return f"Error: {e}"


@app.route('/redirect', methods=['GET'])
def redirect_user():
    """ISSUE: Open redirect vulnerability"""
    next_url = request.args.get('next')
    
    # ISSUE 10: No URL validation - open redirect
    return f'<meta http-equiv="refresh" content="0;url={next_url}">'


@app.route('/math', methods=['POST'])
def calculate():
    """ISSUE: Missing input validation"""
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    
    # ISSUE 11: Division by zero - no validation
    result = a / b
    
    return str(result)


@app.route('/api/data', methods=['GET'])
def get_data():
    """ISSUE: Information disclosure"""
    
    # ISSUE 12: Sensitive data in comments/response
    api_key = "sk_live_51234567890abcdefg"  # Hardcoded API key
    db_password = "postgres_password_123"  # Hardcoded credentials
    
    return {"data": "public", "key": api_key}


class DataProcessor:
    """ISSUE: Complex function with multiple responsibilities"""
    
    def process_and_validate_and_log_and_transform(self, data, source, dest, format, validate=True, log=True, transform=True):
        """ISSUE 13: God function - too many responsibilities"""
        
        # 20 lines of nested logic
        if validate:
            if isinstance(data, dict):
                if 'id' in data:
                    if data['id'] > 0:
                        if 'name' in data:
                            if len(data['name']) > 0:
                                if log:
                                    # Log logic
                                    pass
                                if transform:
                                    # Transform logic
                                    pass
        
        return data


# Global state without synchronization
request_counter = 0

def increment_counter():
    """ISSUE 14: Race condition - no locking"""
    global request_counter
    request_counter += 1  # Not thread-safe


@app.before_request
def log_request():
    """ISSUE 15: No rate limiting - DoS vulnerability"""
    # No rate limiting - anyone can spam requests
    increment_counter()


if __name__ == '__main__':
    app.run(debug=True)  # ISSUE 16: Debug mode in production
