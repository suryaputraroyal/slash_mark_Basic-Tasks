# praksh's encrypt.py
from cryptography.fernet import Fernet
import os

def load_key():
    return open("keys/key.key", "rb").read()

def encrypt_image(image_path):
    key = load_key()
    fernet = Fernet(key)

    with open(image_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("images/encrypted_image.enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

if __name__ == "__main__":
    #replace with acutual path
    image_path = "images/input_image.jpg"
    encrypt_image(image_path)
    print(f"Image {image_path} encrypted and saved as images/encrypted_image.enc")
