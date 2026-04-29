# Лабораторная работа №2: Интерфейсы, Репозиторий, JSON

**Вариант:** Python + SQLite + консольное приложение

## Описание

Проект демонстрирует:
- Применение интерфейсов (ABC) в Python для реализации принципов SOLID.
- Паттерн «Репозиторий» для работы с SQLite (синхронный, асинхронный, Generic, Unit of Work).
- REST API на Flask для CRUD-операций над таблицей `User` с передачей данных в JSON.

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/lab2-interfaces-repository-json.git
   cd lab2-interfaces-repository-json

2. Создайте виртуальное окружение (рекомендуется)
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

3. Установите зависимости:
   pip install -r requirements.txt

   Часть 1. Интерфейсы
Запустите каждый файл по отдельности:
python part1_interfaces/task1_basic.py
python part1_interfaces/task2_inheritance.py
python part1_interfaces/task3_isp.py
python part1_interfaces/task4_polymorphism.py

   Часть 2. Паттерн «Репозиторий»
Запустите демонстрацию:

bash
python part2_repository/demo.py
Будет создана база данных library.db с таблицами Author и Book, добавлены тестовые данные и выполнены операции CRUD.

   Часть 3. REST API (таблица User)
Создайте базу данных users.db:

bash
python part3_rest_api/create_db.py
Запустите Flask-сервер:

bash
python part3_rest_api/app.py
Отправляйте HTTP-запросы (через Postman, curl или встроенный test_api.http). Примеры:

Создание пользователя (POST /user):

json
{
  "login": "alice",
  "PassHash": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
}
Получение пользователя (GET /user/1)

Обновление (PUT /user/1)

Удаление (DELETE /user/1)

Зависимости
Все зависимости перечислены в requirements.txt. Основные:

flask
flask-sqlalchemy
aiosqlite

Лицензия
Учебный проект.
