from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# Trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Trang Caesar Cipher
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

# Mã hóa văn bản Caesar
@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"Input text: {text}<br>Key: {key}<br>Encrypted text: {encrypted_text}"

# Giải mã văn bản Caesar
@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"Cipher text: {text}<br>Key: {key}<br>Decrypted text: {decrypted_text}"

# Trang Vigenere Cipher
@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

# Mã hóa Vigenere
@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = VigenereCipher()
    encrypted_text = cipher.vigenere_encrypt(text, key)
    return f"Input text: {text}<br>Key: {key}<br>Encrypted text: {encrypted_text}"

# Giải mã Vigenere
@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = VigenereCipher()
    decrypted_text = cipher.vigenere_decrypt(text, key)
    return f"Cipher text: {text}<br>Key: {key}<br>Decrypted text: {decrypted_text}"

# Trang Rail Fence Cipher
@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

# Mã hóa Rail Fence
@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = RailFenceCipher()
    encrypted_text = cipher.rail_fence_encrypt(text, key)
    return f"Input text: {text}<br>Key: {key}<br>Encrypted text: {encrypted_text}"

# Giải mã Rail Fence
@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = RailFenceCipher()
    decrypted_text = cipher.rail_fence_decrypt(text, key)
    return f"Cipher text: {text}<br>Key: {key}<br>Decrypted text: {decrypted_text}"

# Trang Playfair Cipher
@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

# Mã hóa Playfair
@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = PlayfairCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return f"Input text: {text}<br>Key: {key}<br>Encrypted text: {encrypted_text}"

# Giải mã Playfair
@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = PlayfairCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return f"Cipher text: {text}<br>Key: {key}<br>Decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
