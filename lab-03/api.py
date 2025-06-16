# Flask API for RSA and ECC cipher operations

from flask import Flask, request, jsonify
from Cipher.rsa import RSACipher
from Cipher.ecc import ECCCipher
import traceback

app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()

# ECC CIPHER ALGORITHM
ecc_cipher = ECCCipher()

# Test route to check if server is working
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'RSA and ECC Cipher API is running',
        'available_endpoints': [
            'GET /api/rsa/generate_keys',
            'POST /api/rsa/encrypt',
            'POST /api/rsa/decrypt', 
            'POST /api/rsa/sign',
            'POST /api/rsa/verify',
            'GET /api/ecc/generate_keys',
            'POST /api/ecc/encrypt',
            'POST /api/ecc/decrypt',
            'POST /api/ecc/sign',
            'POST /api/ecc/verify'
        ]
    })

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'API is working'})

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    try:
        rsa_cipher.generate_keys()
        return jsonify({'message': 'RSA keys generated successfully'})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/api/rsa/encrypt', methods=["POST"])
def rsa_encrypt():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        if 'message' not in data or 'key_type' not in data:
            return jsonify({'error': 'Missing required fields: message, key_type'}), 400
            
        message = data['message']
        key_type = data['key_type']
        private_key, public_key = rsa_cipher.load_keys()
        
        if key_type == 'public':
            key = public_key
        elif key_type == 'private':
            key = private_key
        else:
            return jsonify({'error': 'Invalid key type. Use "public" or "private"'}), 400

        encrypted_message = rsa_cipher.encrypt(message, key)
        encrypted_hex = encrypted_message.hex()
        return jsonify({'encrypted_message': encrypted_hex})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        if 'ciphertext' not in data or 'key_type' not in data:
            return jsonify({'error': 'Missing required fields: ciphertext, key_type'}), 400
            
        ciphertext_hex = data['ciphertext']
        key_type = data['key_type']
        private_key, public_key = rsa_cipher.load_keys()

        if key_type == 'public':
            key = public_key
        elif key_type == 'private':
            key = private_key
        else:
            return jsonify({'error': 'Invalid key type. Use "public" or "private"'}), 400

        ciphertext = bytes.fromhex(ciphertext_hex)
        decrypted_message = rsa_cipher.decrypt(ciphertext, key)
        return jsonify({'decrypted_message': decrypted_message})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign_message():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        if 'message' not in data:
            return jsonify({'error': 'Missing required field: message'}), 400
            
        message = data['message']
        private_key, _ = rsa_cipher.load_keys()
        signature = rsa_cipher.sign(message, private_key)
        signature_hex = signature.hex()
        return jsonify({'signature': signature_hex})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify_signature():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        if 'message' not in data or 'signature' not in data:
            return jsonify({'error': 'Missing required fields: message, signature'}), 400
            
        message = data['message']
        signature_hex = data['signature']
        _, public_key = rsa_cipher.load_keys()
        signature = bytes.fromhex(signature_hex)
        is_verified = rsa_cipher.verify(message, signature, public_key)
        return jsonify({'is_verified': is_verified})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    try:
        ecc_cipher.generate_keys()
        return jsonify({'message': 'ECC keys generated successfully'})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/api/ecc/encrypt', methods=['POST'])
def ecc_encrypt():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        if 'message' not in data:
            return jsonify({'error': 'Missing required field: message'}), 400
            
        message = data['message']
        encrypted_message = ecc_cipher.encrypt(message)
        encrypted_hex = encrypted_message.hex()
        return jsonify({'encrypted_message': encrypted_hex})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/api/ecc/decrypt', methods=['POST'])
def ecc_decrypt():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        if 'ciphertext' not in data:
            return jsonify({'error': 'Missing required field: ciphertext'}), 400
            
        ciphertext_hex = data['ciphertext']
        ciphertext = bytes.fromhex(ciphertext_hex)
        decrypted_message = ecc_cipher.decrypt(ciphertext)
        
        if isinstance(decrypted_message, bytes):
            decrypted_message = decrypted_message.decode()
            
        return jsonify({'decrypted_message': decrypted_message})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        if 'message' not in data:
            return jsonify({'error': 'Missing required field: message'}), 400
            
        message = data['message']
        signature = ecc_cipher.sign(message)
        signature_hex = signature.hex()
        return jsonify({'signature': signature_hex})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        if 'message' not in data or 'signature' not in data:
            return jsonify({'error': 'Missing required fields: message, signature'}), 400
            
        message = data['message']
        signature_hex = data['signature']
        signature = bytes.fromhex(signature_hex)
        
        is_valid = ecc_cipher.verify(message, signature)
        return jsonify({'is_valid': is_valid})
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

# main function
if __name__ == "__main__":
    print("Starting Flask API server...")
    print("Available endpoints:")
    print("  GET  /              - API info")
    print("  GET  /test          - Test endpoint")
    print("  GET  /api/rsa/generate_keys")
    print("  POST /api/rsa/encrypt")
    print("  POST /api/rsa/decrypt")
    print("  POST /api/rsa/sign")
    print("  POST /api/rsa/verify")
    print("  GET  /api/ecc/generate_keys")
    print("  POST /api/ecc/encrypt")
    print("  POST /api/ecc/decrypt")
    print("  POST /api/ecc/sign")
    print("  POST /api/ecc/verify")
    print("\nServer running on: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
