# Bookmark Manager API

REST API для управления закладками с JWT-авторизацией, тегами и поиском.

**Живой сервис (Swagger UI):** [https://booksmark-manager-kraykson1.mia0.amvera.tech/docs](https://booksmark-manager-kraykson1.mia0.amvera.tech/docs)

## 🚀 О проекте

Bookmark Manager — это backend-сервис, который позволяет пользователям:
- Регистрироваться и входить в систему (JWT)
- Создавать, просматривать, редактировать и удалять свои закладки
- Искать закладки по тегам (в разработке)

Проект создан как портфолио для демонстрации навыков Python Backend разработки.

## 🛠️ Технологии

- **Python 3.12**
- **FastAPI** — веб-фреймворк
- **PostgreSQL** — база данных
- **SQLAlchemy** — ORM
- **Alembic** — миграции
- **JWT** (python-jose) — авторизация
- **Pwdlib** (Argon2) — хеширование паролей
- **Docker** + **Docker Compose** — контейнеризация
- **Amvera** — хостинг

## 📦 Установка и запуск

### Локально (через Docker Compose)

1. Клонируйте репозиторий:
   git clone https://github.com/kraykson1/bookmark-manager.git
   cd bookmark-manager

2. Запустите контейнеры:
   docker compose up -d

3. Откройте документацию:
   http://127.0.0.1:8000/docs

### Локально (без Docker)

1. Установите зависимости:
   pip install -r requirements.txt

2. Запустите PostgreSQL и создайте базу bookmarkdb.

3. Укажите DATABASE_URL в app/database.py или через переменную окружения.

4. Запустите сервер:
   uvicorn app.main:app --reload

## 📚 Документация API

После запуска сервера документация доступна по адресу:
- **Swagger UI:** /docs
- **ReDoc:** /redoc

### Основные эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| POST | /auth/register | Регистрация пользователя |
| POST | /auth/login | Вход и получение JWT |
| GET | /bookmarks/ | Все закладки пользователя |
| POST | /bookmarks/ | Создать закладку |
| GET | /bookmarks/{id} | Одна закладка |
| PUT | /bookmarks/{id} | Обновить закладку |
| DELETE | /bookmarks/{id} | Удалить закладку |

## 🧪 Тестирование

(Планируется добавить тесты с pytest)

## 🤝 Вклад

Проект создан в учебных целях. Предложения и пул-реквесты приветствуются.

## 📄 Лицензия

MIT