from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

# Настроим фейковые логин и пароль
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "qwerty123"

# Логи
log_folder = "logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logging.basicConfig(
    filename=os.path.join(log_folder, 'access.log'),
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

@app.route('/')
def index():
    return '''
    <h2>Добро пожаловать на фейковый сервер</h2>
    <p>Отправьте POST-запрос на <code>/login</code> с полями <code>username</code> и <code>password</code></p>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    logging.info(f"Попытка входа: {username} | {password}")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return "Добро пожаловать!", 200
    else:
        return "Неверный логин или пароль", 401

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
