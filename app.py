from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Главный маршрут, который отображает HTML-страницу
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Обработчик для API-вызовов
@app.route('/api/<method>', methods=['POST'])
def call_api(method):
    # Получаем параметры idInstance и apiTokenInstance из запроса
    id_instance = request.json.get('idInstance')
    api_token_instance = request.json.get('apiTokenInstance')
    
    # Формируем URL для вызова API
    url = f'https://api.green-api.com/waInstance{id_instance}/{method}/{api_token_instance}'
    
    # Обрабатываем разные методы API
    if method == 'sendMessage':
        # Если метод - отправка сообщения, получаем данные сообщения и отправляем запрос
        message_data = request.json.get('data')
        response = requests.post(url, json=message_data)
    else:
        # Для других методов выполняем GET-запрос
        response = requests.get(url)
    
    # Возвращаем результат запроса в формате JSON
    return jsonify(response.json())

# Запуск приложения
# if __name__ == '__main__':
#     app.run(debug=True)
