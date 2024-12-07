import requests
from faker import Faker

# URL API
url = "http://api.bsod.fans:44219/user/sign-in"

# Создаём объект Faker
fake = Faker()

# Генерируем случайный email
random_email = fake.email()

# Данные для POST-запроса
form_data = {
    "email": random_email
}

# Отправляем POST-запрос
response = requests.post(url, data=form_data)

# Выводим результат
print(f"Статус-код: {response.status_code}")
print("Ответ сервера:", response.text)
