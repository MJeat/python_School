from cryptography.fernet import Fernet

# Your provided key (as a bytes object)
key = b'0JU1ebOoK7vn2Tl9d0ikbztSbdy6WTKrCeQBtLcbJc8='

# Your provided encrypted message
encrypted_message = b'gAAAAABm_h13xr8IVMv65xsKbOArSmpUTGykNbQSGXX6-gaV25Ynb39Mn5edNIXqkSNHSJbHwdpZCyM-BW9VQkVsAn0YOQRX3A=='

# Create a Fernet object with the key
cipher = Fernet(key)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message).decode()

print("Decrypted message:", decrypted_message)
