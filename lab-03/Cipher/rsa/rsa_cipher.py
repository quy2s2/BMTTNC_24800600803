import os
import rsa

class RSACipher:
    def __init__(self):
        self.public_key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys', 'public.pem')
        self.private_key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys', 'private.pem')
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        """Generate RSA key pair and save to files"""
        (pubkey, privkey) = rsa.newkeys(2048)
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.public_key_path), exist_ok=True)
        
        # Save public key
        with open(self.public_key_path, 'wb') as f:
            f.write(pubkey.save_pkcs1())
        
        # Save private key
        with open(self.private_key_path, 'wb') as f:
            f.write(privkey.save_pkcs1())
        
        self.public_key = pubkey
        self.private_key = privkey
        return pubkey, privkey

    def load_keys(self):
        """Load RSA key pair from files"""
        try:
            with open(self.public_key_path, 'rb') as f:
                public_key_data = f.read()
                public_key = rsa.PublicKey.load_pkcs1(public_key_data)
                
            with open(self.private_key_path, 'rb') as f:
                private_key_data = f.read()
                private_key = rsa.PrivateKey.load_pkcs1(private_key_data)
                
            return private_key, public_key
        except Exception as e:
            print(f"Error loading keys: {str(e)}")
            self.generate_keys()
            return self.private_key, self.public_key

    def encrypt(self, message, key):
        """Encrypt a message using RSA"""
        return rsa.encrypt(message.encode('utf-8'), key)

    def decrypt(self, ciphertext, key):
        """Decrypt a message using RSA"""
        try:
            return rsa.decrypt(ciphertext, key).decode('utf-8')
        except Exception as e:
            print(f"Decryption error: {str(e)}")
            return ""

    def sign(self, message, key):
        """Sign a message using RSA"""
        return rsa.sign(message.encode('utf-8'), key, 'SHA-1')

    def verify(self, message, signature, key):
        """Verify a signature using RSA"""
        try:
            rsa.verify(message.encode('utf-8'), signature, key)
            return True
        except Exception as e:
            print(f"Verification error: {str(e)}")
            return False