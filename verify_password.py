import bcrypt

# The password from the user input
user_input_password = 'my_secure_password'

# The stored hashed password (from the database)
stored_hashed_password = '$2b$12$qHxI9wseNdlHs0WrMRxunejDaCDp7IZc8RtNRlGXsTcX0U8ucv0te'

# Verify if the entered password matches the stored hash
if bcrypt.checkpw(user_input_password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
    print("Password matches")
else:
    print("Password does not match")
