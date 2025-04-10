import time
import os

def generate_report(successful_attempts, failed_attempts):
    # Убедимся, что папка reports существует
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Генерируем имя отчета с датой
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"reports/attack_report_{timestamp}.html"
    
    # Содержимое отчета
    report_content = f"""
    <html>
    <head><title>Отчет об атаке</title></head>
    <body>
        <h1>Отчет о словарной атаке</h1>
        <p><strong>Дата атаки:</strong> {timestamp}</p>
        <p><strong>Успешных попыток:</strong> {len(successful_attempts)}</p>
        <p><strong>Неудачных попыток:</strong> {len(failed_attempts)}</p>
        <p><strong>Общее количество попыток:</strong> {len(successful_attempts) + len(failed_attempts)}</p>
        <hr>
        <h2>Детали атаки:</h2>
        <table border="1">
            <tr><th>Пароль</th><th>Результат</th></tr>
    """

    # Добавляем строки для каждого пароля
    for attempt in successful_attempts:
        report_content += f"<tr><td>{attempt['password']}</td><td>Успех</td></tr>"

    for attempt in failed_attempts:
        report_content += f"<tr><td>{attempt['password']}</td><td>Неудача</td></tr>"

    report_content += """
        </table>
    </body>
    </html>
    """

    # Записываем отчет в файл
    with open(report_filename, 'w') as report_file:
        report_file.write(report_content)

    print(f"Отчет сохранен как {report_filename}")
