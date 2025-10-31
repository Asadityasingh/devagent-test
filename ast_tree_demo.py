def process_payment(amount, user_id):
    query = "INSERT INTO payments VALUES ('" + user_id + "', " + str(amount) + ")"
    return db.execute(query)

STRIPE_KEY = "sk_live2_1234567890abcdef"
