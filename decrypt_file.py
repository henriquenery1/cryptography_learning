from cryptography.fernet import Fernet

# Read the key
key = ''
with open('my_top_secret.key', 'rb') as file:
  key = file.read()

# Read the encrypted data from file
encrypted_data = ''
with open('my_top_secret_info.txt', 'rb') as file:
  encrypted_data = file.read()

# Decrypt the data 
f = Fernet(key)  
decrypt_data = f.decrypt(encrypted_data)

print('Encrypted data: ', encrypted_data.decode())
print()
print('Decrypted data: ', decrypt_data.decode())