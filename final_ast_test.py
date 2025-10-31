def login(user):
 query = "SELECT * FROM users WHERE id = '" + user + "'"
 return db.execute(query)

API_SECRET = "hardcoded-key-12345"
