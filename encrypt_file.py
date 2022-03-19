from cryptography.fernet import Fernet

# Read the key
key = ''
with open('my_top_secret.key', 'rb') as file:
  key = file.read()

# Read data from file
data = ''
with open('to_be_secret.txt', 'rb') as file:
  data = file.read()
print(data)

# Encrypt data
f = Fernet(key)
encrypted_data = f.encrypt(data)
print(encrypted_data)

# Save the encrypted data into a file
with open('my_top_secret_info', 'wb') as file:
  file.write(encrypted_data)


