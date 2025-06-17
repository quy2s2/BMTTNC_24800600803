import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox)
from PyQt5.QtCore import Qt

class AsymCipherForm(QMainWindow):
    def __init__(self, cipher_type):
        super().__init__()
        self.cipher_type = cipher_type
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f"{self.cipher_type} - Phạm Phú Quý - MSSV: 24800600803")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        header = QLabel(f"{self.cipher_type} Encryption/Decryption")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(header)

        info = QLabel("fullname: Phạm Phú Quý + MSSV: 24800600803")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("color: #007bff; font-size: 14px;")
        layout.addWidget(info)

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter text to encrypt/decrypt")
        layout.addWidget(self.input_text)

        if self.cipher_type == "RSA Cipher":
            self.key_input = QLineEdit()
            self.key_input.setPlaceholderText("Enter public/private key or leave blank for default")
            layout.addWidget(self.key_input)
        elif self.cipher_type == "ECC Cipher":
            self.key_input = QLineEdit()
            self.key_input.setPlaceholderText("Enter ECC key or leave blank for default")
            layout.addWidget(self.key_input)
        else:
            self.key_input = QLineEdit()
            self.key_input.setPlaceholderText("Enter key or leave blank for default")
            layout.addWidget(self.key_input)

        self.operation = QComboBox()
        self.operation.addItems(["Encrypt", "Decrypt"])
        layout.addWidget(self.operation)

        self.process_btn = QPushButton("Process")
        self.process_btn.clicked.connect(self.process_text)
        layout.addWidget(self.process_btn)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Result will appear here")
        layout.addWidget(self.result_text)

        self.setGeometry(350, 350, 500, 400)

    def process_text(self):
        input_text = self.input_text.toPlainText()
        key = self.key_input.text()
        operation = self.operation.currentText()
        self.result_text.setText(f"Operation: {operation}\nInput: {input_text}\nKey: {key}\n\nThis is a placeholder result.")

def show_asym_form(cipher_type):
    app = QApplication(sys.argv)
    form = AsymCipherForm(cipher_type)
    form.show()
    app.exec_()

if __name__ == '__main__':
    show_asym_form("RSA Cipher")
