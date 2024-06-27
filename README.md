THE APPROACH TO Task 1 Text Encryption Using Cryptographic Algorithms :

To build a simple web application to encrypt and decrypt text using strong encryption. I have use the Python Flask framework for the web application and the `cryptography` library for encryption and decryption.

### Step-by-Step Guide

#### Step 1: Set up the environment

1. **Install Flask and cryptography:**
   ```
   pip install Flask cryptography
   ```

2. **Create the project structure:**
   ```
   encryption_app/
   ├── app.py
   ├── templates/
   │   └── index.html
   └── static/
       └── styles.css
   ```

#### Step 2: Create the Flask application

**app.py**
```
refer code at app.py in text encryption decryption directory
```

#### Step 3: Create the HTML template

**templates/index.html**
``` refer code at templates/index.html
```

#### Step 4: Add some basic styling

**static/styles.css**
``` refer code at static/styles.css
```

#### Step 5: Run the application

```
python app.py
```

### Explanation

- **Flask Application (app.py):**
  - `Flask` is used to create the web application.
  - `Fernet` from the `cryptography` library is used for symmetric encryption and decryption.
  - The `index` route handles both GET and POST requests.
  - On form submission, the text is encrypted or decrypted based on the button clicked.

- **HTML Template (index.html):**
  - Provides a simple interface for entering text and choosing to encrypt or decrypt it.
  - Displays messages and results using Flask's `flash` messages.

- **CSS (styles.css):**
  - Adds basic styling to make the web app look better.

This setup ensures that the same input produces different encrypted outputs due to the nature of the `Fernet` encryption, which includes a timestamp and uses a unique key each time.





THE APPROACH FOR Task 2 Keylogger Software :

### Key Logger Cybersecurity Project

#### Objective
To create a key logger to understand how they work and develop strategies for detecting and preventing unauthorized key logging.

#### Tools and Technologies
- **Programming Language**: Python
- **Libraries**: `pynput` for capturing keyboard events, `smtplib` for sending logged data via email, `os` and `platform` for system operations
- **Development Environment**: Any Python IDE or text editor
- **Operating System**: Windows/Linux/MacOS

#### Project Steps

1. **Setup Development Environment**
   - Install Python from the [official website](https://www.python.org/).
   - Install `pynput` library using pip:
     ```sh
     pip install pynput
     ```

2. **Create Key Logger Script**
   - Create a Python file named `keylogger.py`.
   - Import necessary libraries:
     ```python
     from pynput import keyboard
     import os
     import smtplib
     from threading import Timer
     import platform
     ```

   - Define a class for the key logger:
     ```
    refer code at keylogger.py
     ```

3. **Run the Key Logger**
   - Run the key logger script:
     ```sh
     python keylogger.py
     ```

4. **Test and Evaluate**
   - Test the key logger in a controlled environment.
   - Ensure you have permission if testing on someone else's machine.
   - Evaluate how the key logger captures keystrokes and sends them to your email.

5. **Detection and Prevention**
   - Research methods to detect key loggers on your system.
   - Implement a basic script to scan for key logger behavior.
   - Educate users on the importance of using antivirus software and keeping systems updated.

6. **Ethical Considerations**
   - Always use the key logger ethically and legally.
   - Inform users and obtain explicit permission before logging keystrokes.
   - Use the knowledge gained to improve cybersecurity practices and awareness.

### Conclusion
This project provides me a hands-on approach to understanding key loggers. By creating and analyzing a key logger, i gain insights into how they operate and how to defend against them. Always prioritize ethical use and legal compliance in all cybersecurity practices.







THE APPROACH FOR Image Encryption :

### Image Encryption Project

In this project, i have encrypt and decrypt images using a secure key.  i have  used the Python library `cryptography` for this purpose, which provides strong encryption algorithms.

### Project Structure

Here's how your project structure will look:

```
image_encryption/
├── encrypt.py
├── decrypt.py
├── keys/
│   ├── key.key
├── images/
│   ├── input_image.jpg
│   └── encrypted_image.enc
│   └── decrypted_image.jpg
```

### Step-by-Step Guide

#### Step 1: Install Required Libraries
Make sure you have the `cryptography` library installed. We can install it using pip:

```
pip install cryptography
```

#### Step 2: Generate a Key
First, we'll generate a key that will be used for encryption and decryption. This key needs to be stored securely.

```
# refer code at generate_key.py

```

Run this script once to generate a key:

```
python generate_key.py
```

#### Step 3: Encryption Script
I have created a script to encrypt an image.

```
# refer code at encrypt.py

```

#### Step 4: Decryption Script
I have created a script to decrypt the image.

```python
# refer code at decrypt.py
```

### Explanation

1. **Key Generation (`generate_key.py`)**:
   - Generates a key using `Fernet.generate_key()`.
   - Saves the key in a file named `key.key`.

2. **Encryption (`encrypt.py`)**:
   - Loads the key from `key.key`.
   - Reads the input image file as bytes.
   - Encrypts the image bytes using `Fernet.encrypt()`.
   - Saves the encrypted data to a file named `encrypted_image.enc`.

3. **Decryption (`decrypt.py`)**:
   - Loads the key from `key.key`.
   - Reads the encrypted file as bytes.
   - Decrypts the image bytes using `Fernet.decrypt()`.
   - Saves the decrypted data to a file named `decrypted_image.jpg`.

### Usage

1. **Encrypt an Image**:
   Place your image (e.g., `input_image.jpg`) in the `images` directory and run:
   ```
   python encrypt.py
   ```

2. **Decrypt an Image**:
   Ensure the encrypted image (`encrypted_image.enc`) is in the `images` directory and run:
   ```
   python decrypt.py
   ```

This project has gave me a lot of understanding about encrypting and decrypting images, introducing me to fundamental cryptographic concepts. Ensure that the key (`key.key`) is kept secure, as anyone with access to this key can decrypt the encrypted images.
