# Доска объявлений

## Описание проекта

Проект представляет собой backend-часть для сайта объявлений.

Бэкенд-часть проекта предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

## Основыне зависимости

1. Python 3.12
2. Django 5.1.1
3. Django REST Framework 3.15.2
4. PostgreSQL 16

## Для запуска проекта выполните следующие шаги:

1. Заполнить файл .env.sample, переименовав его в .env
2. В терминале выполнить команду *docker-compose up -d --build*

## API Документация

- Swagger UI доступен по адресу: /swagger/
- Redoc доступен по адресу: /redoc/