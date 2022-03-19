from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

with open('my_top_secret.key', 'wb') as file:
  file.write(key)