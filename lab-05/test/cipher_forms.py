import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox)
from PyQt5.QtCore import Qt

class CipherForm(QMainWindow):
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
        layout.addWidget(header)

        # Common widgets for all forms
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter text to encrypt/decrypt")
        layout.addWidget(self.input_text)

        # Specific widgets based on cipher type
        if self.cipher_type == "Caesar Cipher":
            self.key_input = QLineEdit()
            self.key_input.setPlaceholderText("Enter shift value (0-25)")
            layout.addWidget(self.key_input)

        elif self.cipher_type == "Vigenere Cipher":
            self.key_input = QLineEdit()
            self.key_input.setPlaceholderText("Enter key (text)")
            layout.addWidget(self.key_input)

        elif self.cipher_type == "Playfair Cipher":
            self.key_input = QLineEdit()
            self.key_input.setPlaceholderText("Enter key (text)")
            layout.addWidget(self.key_input)

        elif self.cipher_type == "Rail Fence Cipher":
            self.key_input = QLineEdit()
            self.key_input.setPlaceholderText("Enter number of rails")
            layout.addWidget(self.key_input)

        # Operation selection
        self.operation = QComboBox()
        self.operation.addItems(["Encrypt", "Decrypt"])
        layout.addWidget(self.operation)

        # Process button
        self.process_btn = QPushButton("Process")
        self.process_btn.clicked.connect(self.process_text)
        layout.addWidget(self.process_btn)

        # Result display
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Result will appear here")
        layout.addWidget(self.result_text)

        # Set window geometry
        self.setGeometry(300, 300, 500, 400)

    def process_text(self):
        # Placeholder for encryption/decryption logic
        input_text = self.input_text.toPlainText()
        key = self.key_input.text()
        operation = self.operation.currentText()

        # Here you would implement the actual cipher logic
        # For now, we'll just show a placeholder result
        self.result_text.setText(f"Operation: {operation}\nInput: {input_text}\nKey: {key}\n\nThis is a placeholder result.")

def show_cipher_form(cipher_type):
    app = QApplication(sys.argv)
    form = CipherForm(cipher_type)
    form.show()
    app.exec_()

if __name__ == '__main__':
    # Test with Caesar Cipher
    show_cipher_form("Caesar Cipher")
