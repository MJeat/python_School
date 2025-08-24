
'''
Note: This is use to see the key and to encrypt your messages or file

'''

from cryptography.fernet import Fernet
# Generate and save the key (only do this once, comment this out after first run)
# def generate_and_save_key():
#     key = Fernet.generate_key()
#     with open("my.key", "wb") as key_file:
#         key_file.write(key)
#     print("Key saved to my.key")
# generate_and_save_key() # If you want to update the key, uncomment generate_and_save_key()

# Load the key from the file
def load_key():
    with open("my.key", "rb") as key_file:
        key = key_file.read()
    return key

# Use the saved key 
key = load_key()
cipher = Fernet(key)

# Encrypt the message (convert string to bytes before encryption)
message = "Hello, you are retarded-sincerely, Zombie"
encrypted_message = cipher.encrypt(message.encode())


# Decrypt the message (convert bytes back to string after decryption)
# decrypted_message = cipher.decrypt(encrypted_message).decode()



print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
# print(f"Decrypted message: {decrypted_message}")
print('This is the key you loaded from the file: ', key)
