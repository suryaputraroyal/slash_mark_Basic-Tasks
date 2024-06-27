# praksh's decrypt.py
from cryptography.fernet import Fernet
import os

def load_key():
    return open("keys/key.key", "rb").read()

def decrypt_image(encrypted_path):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_path, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open("images/decrypted_image.jpg", "wb") as dec_file:
        dec_file.write(decrypted)

if __name__ == "__main__":
    #replace with your actual path
    encrypted_path = "images/encrypted_image.enc"
    decrypt_image(encrypted_path)
    print(f"Encrypted image {encrypted_path} decrypted and saved as images/decrypted_image.jpg")
