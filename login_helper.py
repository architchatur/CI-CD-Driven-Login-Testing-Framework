def is_valid_username(username):
    return username.isalnum() and len(username) > 5

def is_valid_password(password):
    return len(password) >= 8

