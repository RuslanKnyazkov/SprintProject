# **Pereval API**  
REST API для управления данными о горных перевалах

---

## **📌 Оглавление**
1. [Функциональность](#-функциональность)
2. [Технологии](#-технологии)
3. [Установка](#-установка)
4. [Документация API](#-документация-api)
5. [Примеры запросов](#-примеры-запросов)
6. [Авторы](#-авторы)

---

## **🎯 Функциональность**
- Создание, чтение, обновление данных о перевалах
- Поддержка вложенных данных:
  - Координаты (`latitude`, `longitude`, `height`)
  - Пользователи (`name` `fam` `oct` `email`, `phone`)
  - Фотографии (`title`, `img`)

---

## **🛠 Технологии**
- **Backend**: Django + DRF (Django Rest Framework)
- **База данных**: PostgreSQL

---

## **⚙️ Установка**
### 1. Клонируйте репозиторий
```bash
git clone https://github.com/RuslanKnyazkov/SprintProject
cd SprintProject/myproject
```

### 2. Создайте виртуальное окружение и установите зависимости
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

``` Ошибка распаковки
Может возникнуть ошибка Failed building wheel for psycopg2
Для этого сделайте следующие шаги
```
```bash
sudo apt-get update
sudo apt-get install python3-dev libpq-dev
```

### 3. Создайте файл .env для информации
```Variables
FSTR_DB_HOST='localhost'(Default)
FSTR_DB_PORT='5432'(Default)
FSTR_DB_LOGIN=?
FSTR_DB_PASS=?
FSTR_DB_NAME=?
SECRET_KEY=?
```

### 4. Создайте секретный ключ
```bash
django-admin shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
- Используйте его для добавление в переменую файла .env SECRET_KEY

### 5. Настройте базу данных
- Создайте базу данных
- Создайте пользователя и пароль
- Добавьте информацию в файл .env
  
```bash
python manage.py migrate
```

### 6. Запустите сервер
```bash
python manage.py runserver
```
Сервер будет доступен по адресу: [http://localhost:8000](http://localhost:8000)

---

### Основные эндпоинты:
| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| `GET` | `/submitData/` | Список всех перевалов |
| `POST` | `/submitData/` | Добавить новый перевал |
| `GET` | `/submitData//{id}/` | Получить данные перевала по ID |
| `PATCH` | `/submitData/{id}/` | Обновить данные перевала (частично) |
| `GET` | `/submitData/user__email={email}/` | Фильтр по email пользователя |

---

## **📡 Примеры запросов**
### 1. Добавление нового перевала (`POST /submitData/`)
```json
{
  "user": {
    "email": "test@example.com",
    "phone": "+79131234567"
  },
  "coords": {
    "latitude": "45.3842",
    "longitude": "7.1525",
    "height": "1200"
  },
  "images": [
    {
      "title": "Вид с вершины",
      "img": "https://example.com/photo1.jpg"
    }
  ]
}
```

### 2. Обновление данных (`PATCH /submitData/1/`)
```json
{
  "status": "accepted",
  "coords": {
    "height": "1250"
  }
}
```

### 3. Фильтр по email пользователя (`GET /submitData/user__email=test@example.com/`)
Возвращает все перевалы, добавленные указанным пользователем.

---
