from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для всех доменов

# Переменная для хранения IP-адреса
current_ip = ''

@app.route('/api/update_ip', methods=['POST'])
def update_ip():
    global current_ip
    data = request.json
    current_ip = data.get('ip', '')
    return jsonify({'status': 'success', 'ip': current_ip})

@app.route('/api/ip', methods=['GET'])
def get_external_ip():
    return jsonify({'ip': current_ip})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)