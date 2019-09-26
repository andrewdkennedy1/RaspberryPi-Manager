from flask import Flask
from flask import url_for, jsonify, render_template, redirect
from refresh import *
from reboot import *
import time
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/refresh', methods=['POST'])
def refresh():
    rf2()
    return "refresh sent -main.py"
    

@app.route('/reboot', methods=['POST'])
def reboot():
    rb2()
    return "reboot sent -main.py"

#access webpage from http://localhost:8081 or whatever port you set below. 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
