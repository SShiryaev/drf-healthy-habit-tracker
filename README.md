# drf-healthy-habit-tracker

## О проекте:
Бэкенд-часть SPA веб-приложения, трекера полезных привычек. Вы можете создавать привычки,
выбирать периодичность, время их выполнения и прочее.
Также, можно получать оповещения о привычке в telegram.

## Контекст проекта:
В 2018 году Джеймс Клир написал книгу «Атомные привычки»,
которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек.


## Основные зависимости:
- python = "^3.12"
- django = "^5.0.6"
- psycopg2-binary = "^2.9.9"
- pillow = "^10.3.0"
- djangorestframework = "^3.15.2"
- python-dotenv = "^1.0.1"
- djangorestframework-simplejwt = "^5.3.1"
- drf-yasg = "^1.21.7"
- setuptools = "^70.1.1"
- django-cors-headers = "^4.4.0"
- celery = "^5.4.0"
- eventlet = "^0.36.1"
- redis = "^5.0.7"
- django-celery-beat = "^2.6.0"
- coverage = "^7.5.4"
- flake8 = "^7.1.0"
<li>Полный список зависимостей находится в poetry.lock</li>

## Для запуска проекта:
- установить зависимости из pyproject.toml
- убрать .sample из .env.sample
- в .env добавить соответствующие значения
- в терминале запустить проект:
```text
python manage.py runserver
```

## Для запуска отложенных и периодических задач:
- запустить redis:
```text
redis-server
```
- запустить фоновую задачу на отправку уведомлений пользователям в telegram чат: https://t.me/sh_habit_bot
```text
celery -A config worker -l INFO  # Для Unix систем
celery -A config worker -l INFO -P eventlet  # Для Windows
celery -A config beat -l info
```

## Для запуска проекта локально воспользуйтесь командой:
  ```text
  python manage.py runserver
  ```
   перейдите на URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)

- Для запуска Celery воспользуйтесь командами:

worker:
    ```
    celery -A config worker -l INFO
    ```

beat:
    ```
    celery -A config beat -l INFO -S django
    ```

### Для запуска проекта через Docker:

- установите Docker себе в систему, перейдя по [ссылке](https://docs.docker.com/engine/install/)
- для сборки проекта и запуска введите команду:

```text
docker-compose up -d --build
```

- перейдите на URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)
=======
