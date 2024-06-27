from flask import Flask, render_template, request, flash
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Using os.urandom for a more secure secret key

# Generate a key for encryption and decryption
# You must keep this key safe; it's the only way to decrypt the data.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            action = request.form.get('action')
            text = request.form.get('text')

            if action == 'encrypt':
                encrypted_text = cipher_suite.encrypt(text.encode()).decode()
                flash('Text successfully encrypted!', 'success')
                return render_template('index.html', original_text=text, result_text=encrypted_text)
            
            elif action == 'decrypt':
                try:
                    decrypted_text = cipher_suite.decrypt(text.encode()).decode()
                    flash('Text successfully decrypted!', 'success')
                    return render_template('index.html', original_text=text, result_text=decrypted_text)
                except Exception as e:
                    flash(f'Error decrypting text: {str(e)}', 'danger')

        return render_template('index.html')

    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
