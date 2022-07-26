# Проект Foodgram
Foodgram, «Продуктовый помощник».
Онлайн-сервис и API для него. На этом сервисе пользователи после регистрации могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать список продуктов, необходимых для приготовления выбранных блюд.

![example workflow](https://github.com/mir32/foodgram-project-react/actions/workflows/workflow.yml/badge.svg)

Проект доступен по следующему адресу: <http://51.250.96.8/recipes/>

Админка (login: admin, password: admin) - <http://51.250.96.8/admin/>

API - <http://51.250.96.8/api/>

Документация API - <http://51.250.96.8/api/docs/>


### Технологии
- Python 3.7
- Django 3.2.13
 - Gunicorn
 - Nginx
 - Docker
 - PostgreSQL

# Шаблон наполнения env-файла

    SECRET_KEY=<seckret_key>
    ALLOWED_HOSTS=<allowed HOSTs>
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=<The name of the database, for example 'postgres'>
    POSTGRES_USER=<Database user name, for example "postgres">
    POSTGRES_PASSWORD=<Database user password>
    DB_HOST=db
    DB_PORT=5432

# Запуск приложения в контейнерах Docker
Клонируйте проект:

```bash
git clone https://github.com/mariao-max/foodgram-project-react.git

```
Перейдите в папку infra и выполните команду, что бы собрать контейнер:
```bash
cd infra
docker-compose up -d
```
Далее выполните следующие команды:

```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput 
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
```

Дополнительно можно наполнить DB ингредиентами и тэгами:

```bash
sudo docker-compose exec backend python manage.py load_tags
sudo docker-compose exec backend python manage.py load_ingrs
```

# Шаблон наполнения env-файла

    SECRET_KEY=<seckret_key>
    ALLOWED_HOSTS=<allowed HOSTs>
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=123456
    DB_HOST=db
    DB_PORT=5432
```