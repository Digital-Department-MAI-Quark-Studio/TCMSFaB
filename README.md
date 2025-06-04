# Система управления конвентом для блога

## 🧰 Технологический стек

- **Язык программирования**: Python 3
- **Бэкенд-фреймворк**: Django 5.1.1
- **Фронтенд**: HTML, CSS, Bootstrap 5
- **Интеграция Bootstrap**: django-bootstrap5==24.3

## 🚀 Быстрый запуск проекта (локально)

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Создать и активировать виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install django==5.1.1 django-bootstrap5==24.3
```

### 4. Применить миграции базы данных

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Создать администратора

```bash
python manage.py createsuperuser
```

> Введите логин, email (можно оставить пустым) и пароль для доступа к админке.

### 6. Запустить сервер разработки

```bash
python manage.py runserver
```

Теперь проект доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🛠 Дополнительно

- Панель администратора доступна по адресу: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- Убедитесь, что у вас установлен Python 3.8+ и pip

---

> Разработано как система управления конвентом для блога: администрирование, публикации, интерфейс на Bootstrap.

