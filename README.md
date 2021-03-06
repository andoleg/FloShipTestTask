# Store - Warehouse backend

### Ссылки

- Админка на стейджинге - [если будет стейджинг]

### Архитектура
Проект содержит в себе два подпроекта – `Store` и `Warehouse` applications.
Общая логика размещена в папке core для уменьшения дупликации кода. \
`Store` - реализует модели, сериализаторы и вьюсеты для стора \
`Warehouse` - реализует модели, сериализаторы и вьюсеты для Warehouse \
Для общения были реализовны Create/Update методы для простоты и наглядности. \
Проект использует `celery` для исполнения фоновых задач, таких как отправка запросов друг другу. Таким образом,
при сохранении объекта, например, не нужно будет ждать serverTimeoutError (бывает и такое). Объект успешно сохранится, а 
отправка запроса произойдет асинхронно. \

После сохранения нового обьекта в админке (только в админке), запрос отправляется на клиента, где по токену идет проверка
и апдейт.

Подобие токенов в django было реализовано через `secrets`. Для общения Store и Warehouse нужно указать их собственные ключи
друг другу (в админке).



### Запуск проекта локально

Проект использует `poetry` для менеджмента зависимостей и virtualenv'ов и docker для бд.
Прежде всего нужно установить его - [ссылка на доку](https://poetry.eustace.io/docs/) 
      
      $ pip install poetry

Далее:

1. Установка всех зависимостей

       $ poetry install

2. Применение virtualenv (если необходимо)

       $ poetry shell

3. Запуск зависимостей (postgres, rabbitmq)

       $ docker-compose up -d

4. Окружение для серверов (в 2х окнах терминала):

   4.1. Конфигурация окружения для `storeapp`

       $ export $(grep -v "^#" storeapp/.env.local | xargs)

   4.2. Конфигурация окружения для `warehouse`

       $ export $(grep -v "^#" warehouse/.env.local | xargs)

5. Запуск веб-сервера
   
       $ python3 manage.py runserver 8000 (any other port for second app)

6. Запуск `celery`

       $ celery -A core.celery_app worker -l info
       
7. Создание суперюзера для каждого сервера

       $ python manage.py createsuperuser --email admin@example.com --username admin
       
8. После запуска двух серверов, необходимо внутри их админок создать обьекты Warehouse и Store

   8.1. IP в формате `http://127.0.0.1:port`
   
   8.2. При создании обьекта Warehouse/Store автоматически генерируется сервер токен. Его нужно указать в поле "Client token" у всех соответсвующих клиентов. И наоборот "Server token" клиента передать серверу.


       
### Используемые env-переменные

* `STORE_DB_HOST` - хост бд
* `STORE_CELERY_BROKER_URL` - адрес брокера для celery
* `SETTINGS_MODULE` - расположение settings.py для запуска разных проектов из одного manage.py
