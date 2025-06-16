from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
import os

class ECCCipher:
    def __init__(self):
        self.curve = ec.SECP256K1()
        self.private_key = None
        self.public_key = None
        self.keys_dir = os.path.join(os.path.dirname(__file__), 'keys')
        
        if not os.path.exists(self.keys_dir):
            os.makedirs(self.keys_dir)

    def generate_keys(self):
        """Generate a new ECC key pair"""
        self.private_key = ec.generate_private_key(self.curve)
        self.public_key = self.private_key.public_key()
        
        # Save the keys
        self._save_keys()
        
    def _save_keys(self):
        """Save the keys to files"""
        if not self.private_key or not self.public_key:
            raise ValueError("Keys must be generated first")
            
        # Save private key
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(os.path.join(self.keys_dir, 'ecc_private.pem'), 'wb') as f:
            f.write(private_pem)
            
        # Save public key
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(os.path.join(self.keys_dir, 'ecc_public.pem'), 'wb') as f:
            f.write(public_pem)

    def load_keys(self):
        """Load keys from files"""
        private_key_path = os.path.join(self.keys_dir, 'ecc_private.pem')
        public_key_path = os.path.join(self.keys_dir, 'ecc_public.pem')
        
        try:
            # Load private key
            with open(private_key_path, 'rb') as f:
                private_pem = f.read()
                self.private_key = serialization.load_pem_private_key(
                    private_pem,
                    password=None
                )
                
            # Load public key
            with open(public_key_path, 'rb') as f:
                public_pem = f.read()
                self.public_key = serialization.load_pem_public_key(public_pem)
                
            return self.private_key, self.public_key
            
        except FileNotFoundError:
            raise Exception("Keys not found. Generate keys first.")

    def sign(self, message):
        """Sign a message using ECDSA"""
        if not self.private_key:
            self.load_keys()
            
        if isinstance(message, str):
            message = message.encode()
            
        signature = self.private_key.sign(
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return signature

    def verify(self, message, signature):
        """Verify a signature using ECDSA"""
        if not self.public_key:
            self.load_keys()
            
        if isinstance(message, str):
            message = message.encode()
            
        try:
            self.public_key.verify(
                signature,
                message,
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except InvalidSignature:
            return False

    def encrypt(self, message):
        """
        Encrypt a message using ECIES
        (Elliptic Curve Integrated Encryption Scheme)
        """
        if not self.public_key:
            self.load_keys()
            
        if isinstance(message, str):
            message = message.encode()

        # Generate an ephemeral key pair
        ephemeral_private_key = ec.generate_private_key(self.curve)
        ephemeral_public_key = ephemeral_private_key.public_key()
        
        # Perform key exchange
        shared_key = ephemeral_private_key.exchange(
            ec.ECDH(),
            self.public_key
        )
        
        # Derive encryption key using HKDF
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
        ).derive(shared_key)
        
        # TODO: Implement actual encryption using the derived key
        # For now, we'll just return the derived key and message
        return derived_key + message

    def decrypt(self, ciphertext):
        """
        Decrypt a message using ECIES
        (Elliptic Curve Integrated Encryption Scheme)
        """
        if not self.private_key:
            self.load_keys()
            
        # Extract the derived key and message
        derived_key = ciphertext[:32]
        message = ciphertext[32:]
        
        # TODO: Implement actual decryption using the derived key
        # For now, we'll just return the message
        return message
