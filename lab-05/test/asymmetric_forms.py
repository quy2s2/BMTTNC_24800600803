import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox,
                           QFileDialog, QHBoxLayout)
from PyQt5.QtCore import Qt

class AsymmetricCipherForm(QMainWindow):
    def __init__(self, cipher_type):
        super().__init__()
        self.cipher_type = cipher_type
        self.initUI()

    def initUI(self):
        # Set window title with student info
        self.setWindowTitle(f"{self.cipher_type} - Phạm Phú Quý - MSSV: 24800600803")
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add header label
        header = QLabel(f"{self.cipher_type} Encryption/Decryption")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 16pt; font-weight: bold; margin: 10px;")
        layout.addWidget(header)

        # Input text area
        input_label = QLabel("Input Text:")
        layout.addWidget(input_label)
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter text to encrypt/decrypt")
        layout.addWidget(self.input_text)

        # Key management section
        key_layout = QHBoxLayout()
        
        # Public key section
        public_key_layout = QVBoxLayout()
        self.public_key_path = QLineEdit()
        self.public_key_path.setPlaceholderText("Public Key Path")
        self.public_key_btn = QPushButton("Select Public Key")
        self.public_key_btn.clicked.connect(lambda: self.select_key_file("public"))
        public_key_layout.addWidget(QLabel("Public Key:"))
        public_key_layout.addWidget(self.public_key_path)
        public_key_layout.addWidget(self.public_key_btn)
        key_layout.addLayout(public_key_layout)

        # Private key section
        private_key_layout = QVBoxLayout()
        self.private_key_path = QLineEdit()
        self.private_key_path.setPlaceholderText("Private Key Path")
        self.private_key_btn = QPushButton("Select Private Key")
        self.private_key_btn.clicked.connect(lambda: self.select_key_file("private"))
        private_key_layout.addWidget(QLabel("Private Key:"))
        private_key_layout.addWidget(self.private_key_path)
        private_key_layout.addWidget(self.private_key_btn)
        key_layout.addLayout(private_key_layout)

        layout.addLayout(key_layout)

        # Additional parameters for ECC
        if self.cipher_type == "ECC":
            self.curve_select = QComboBox()
            self.curve_select.addItems(["secp256k1", "secp384r1", "secp521r1"])
            curve_label = QLabel("Select Curve:")
            layout.addWidget(curve_label)
            layout.addWidget(self.curve_select)

        # Operation selection
        self.operation = QComboBox()
        self.operation.addItems(["Encrypt", "Decrypt"])
        layout.addWidget(QLabel("Operation:"))
        layout.addWidget(self.operation)

        # Generate Keys Button
        self.generate_keys_btn = QPushButton("Generate New Key Pair")
        self.generate_keys_btn.clicked.connect(self.generate_keys)
        layout.addWidget(self.generate_keys_btn)

        # Process button
        self.process_btn = QPushButton("Process")
        self.process_btn.clicked.connect(self.process_text)
        self.process_btn.setStyleSheet("background-color: #007bff; color: white; padding: 10px;")
        layout.addWidget(self.process_btn)

        # Result display
        layout.addWidget(QLabel("Result:"))
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Result will appear here")
        layout.addWidget(self.result_text)

        # Set window geometry
        self.setGeometry(300, 300, 800, 600)

    def select_key_file(self, key_type):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            f"Select {key_type.title()} Key File",
            "",
            "PEM Files (*.pem);;All Files (*.*)"
        )
        if file_name:
            if key_type == "public":
                self.public_key_path.setText(file_name)
            else:
                self.private_key_path.setText(file_name)

    def generate_keys(self):
        # Placeholder for key generation functionality
        if self.cipher_type == "RSA":
            self.result_text.setText("RSA key pair generation would happen here")
        else:
            curve = self.curve_select.currentText()
            self.result_text.setText(f"ECC key pair generation would happen here using curve {curve}")

    def process_text(self):
        # Placeholder for encryption/decryption functionality
        input_text = self.input_text.toPlainText()
        operation = self.operation.currentText()
        
        if self.cipher_type == "RSA":
            result = f"RSA {operation.lower()}ion would happen here"
        else:
            curve = self.curve_select.currentText()
            result = f"ECC {operation.lower()}ion would happen here using curve {curve}"
            
        self.result_text.setText(result)

def show_cipher_form(cipher_type):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Modern style
    form = AsymmetricCipherForm(cipher_type)
    form.show()
    app.exec_()

if __name__ == '__main__':
    # Test with RSA Cipher
    show_cipher_form("RSA")
