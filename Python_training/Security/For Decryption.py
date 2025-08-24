
'''
Note: This is use to decrypt messages or files

'''


from cryptography.fernet import Fernet

# Your friend's provided key (as a bytes object). Paste it in the string ''
Friend_key = b' '

# Your friend's provided encrypted message. Paste it in the string ''
encrypted_message = b' '

# Create a Fernet object with the key
cipher = Fernet(Friend_key)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message).decode()

print("Decrypted message:", decrypted_message)
