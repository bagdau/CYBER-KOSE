from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Предустановленный логин и пароль
correct_username = "admin"
correct_password = "password123"

# Папка для логов
log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, "access.log")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Логируем попытки входа
    with open(log_file, "a") as log:
        log.write(f"Username: {username}, Password: {password}\n")
    
    if username == correct_username and password == correct_password:
        return jsonify({"status": "success", "message": "Login successful!"}), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
