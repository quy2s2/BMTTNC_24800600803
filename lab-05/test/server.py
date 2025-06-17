from flask import Flask, render_template, send_from_directory
import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication

app = Flask(__name__, static_folder='static', template_folder='templates')

def open_ui(ui_script):
    try:
        lab03_ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'lab-03', 'ui')
        process = subprocess.Popen([sys.executable, ui_script], 
                                cwd=lab03_ui_path)
        return process
    except Exception as e:
        print(f"Error opening UI: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    open_ui('caesar_cipher.py')
    return '', 204

@app.route('/rsa')
def rsa():
    open_ui('rsa.py')
    return '', 204

@app.route('/ecc')
def ecc():
    open_ui('ecc_cipher.py')
    return '', 204

def run_server():
    print("Server running at http://localhost:5000")
    print("Student: Phạm Phú Quý")
    print("MSSV: 24800600803")
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    run_server()
