import bcrypt

# Replace this with the password you want to hash
password = 'my_secure_password' 

# Generate salt and hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Output the hashed password
print(hashed_password.decode('utf-8'))
