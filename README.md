# Необходимо разработать API реализующий CRUD операции.

## Сервис располагается на собственном VDS-сервере, реализован на DRF с использованием PostgreSQL, uwsgi, nginx.

*P.S. Иногда возможны перебои в работе сервера, из-за загрузки других проектов и предоставления им онлайн-жизни.*

### Функционал:

1. Регистрация пользователя.
2. Авторизация пользователя. (Используется JWT авторизация)
3. Добавление новой задачи.
4. Изменение задачи.
5. Удаление задачи.
6. Список задач.
7. Список задач, созданных текущим пользователем.

### Описание работы веб-сервиса:

* http://95.217.64.252:81/api/v1/registr/

Принимает POST запрос в виде:

```
{
  "email": "test@example.com",
  "password": "123456789",
  "first_name": "Artur",
  "last_name": "Kalimullin"
}
```

В случае успешного запроса сервер ответит:

```
{
  'success': 'True',
  'status code': 201,
  'message': 'User registered  successfully'
}
```

* http://95.217.64.252:81/api/v1/login/

Принимает POST запрос в виде:

```
{
  "email": "test@example.com",
  "password": "123456789"
}
```

В случае успешного запроса (пользователь зарегистрирован и пароль правильный) сервер ответит:

```
{
  "access": "token1",
  "refresh": "token2"
}
```

Токен `access` необходим для последующих дальнейшей работы. Токен `refresh` необходим для обновления токена по url `http://95.217.64.252:81/api/v1/token/refresh/`

* http://95.217.64.252:81/api/v1/token/refresh/

Принимает POST запрос с токеном `refresh`. В случае успешного запроса отправляет токен `access`, который необходим для последующих дальнейшей работы, и токен `refresh`, который необходим для обновления токена.

* http://95.217.64.252:81/api/v1/task/create/

Принимает POST запрос c токеном `access` в виде:

```
{
  "id_workers": "1, 2",
  "title": "Test task",
  "description": "Hahhahahahahahah",
  "completion_date": "2022-07-22 12:00"
}
```

В случае успешного запроса отвечает

```
{
  "id_workers": "1, 2",
  "title": "Test task",
  "description": "Hahhahahahahahah",
  "completion_date": "2022-07-22 12:00",
  "owner": "t@example.com",

}
```

* http://95.217.64.252:81/api/v1/task/all/

Принимает GET запрос c токеном `access`.

Выводит все имеющиеся задачи в виде:

```
{
  "id": 1
  "id_workers": "1, 2",
  "title": "Test task",
  "description": "Hahhahahahahahah",
  "completion_date": "2022-07-22 12:00",
  "owner": "t@example.com",

}
```

* http://95.217.64.252:81/api/v1/task/my/

Принимает GET запрос c токеном `access`.

Выводит задачи, которые создал только пользователь, который запрашивает.

* http://95.217.64.252:81/api/v1/task/detail/:pk/

Принимает GET, PUT, DELETE, PATCH запрос c токеном `access` и переменной pk (являющейся id задачи). Разрешает запрос только, если пользователь является создателем данных задач.

### По url http://95.217.64.252:81/redoc/ и http://95.217.64.252:81/swagger/ доступна OPEN API спецификация.

### Коллекция [POSTMAN]()

### Настройки NGINX и UWSGI

```
[uwsgi]
chdir = /home/kokoc/task_from_nti/user_task
env = DJANGO_SETTINGS_MODULE = user_task.settings
wsgi-file = /home/kokoc/task_from_nti/user_task/user_task/wsgi.py
workers = 1
plugins = python3
home=/home/kokoc/task_from_nti/venv/
pythonpath = /var/work/venv/lib/python3.8/site-packages
socket = /run/uwsgi/app/django/socket
uid = www-data
gui = www-data


```

```
server {
    listen __;
    server_tokens off;
    server_name ____;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:///run/uwsgi/app/django/socket;
    }
  
    location /static/ {
        alias /home/kokoc/task_from_nti/user_task/user_task/static/;
    }

}


```
