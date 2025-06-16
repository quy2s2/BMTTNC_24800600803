# rsa_cipher.py

import os
import rsa

class RSACipher:
    def __init__(self):
        self.keys_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys')
        if not os.path.exists(self.keys_dir):
            os.makedirs(self.keys_dir)
    
    def generate_keys(self):
        pubkey, privkey = rsa.newkeys(2048)
        
        with open(os.path.join(self.keys_dir, 'public.pem'), 'wb') as f:
            f.write(pubkey.save_pkcs1('PEM'))
        
        with open(os.path.join(self.keys_dir, 'private.pem'), 'wb') as f:
            f.write(privkey.save_pkcs1('PEM'))
    
    def load_keys(self):
        with open(os.path.join(self.keys_dir, 'private.pem'), 'rb') as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
        
        with open(os.path.join(self.keys_dir, 'public.pem'), 'rb') as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        
        return private_key, public_key
    
    def encrypt(self, message, key):
        if isinstance(message, str):
            message = message.encode('utf-8')
        return rsa.encrypt(message, key)
    
    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('utf-8')
        except Exception as e:
            return str(e)
    
    def sign(self, message, key):
        if isinstance(message, str):
            message = message.encode('utf-8')
        return rsa.sign(message, key, 'SHA-1')
    
    def verify(self, message, signature, key):
        if isinstance(message, str):
            message = message.encode('utf-8')
        try:
            return rsa.verify(message, signature, key) == 'SHA-1'
        except rsa.VerificationError:
            return False
