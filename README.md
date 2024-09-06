# Телеграмм бот для просмотра стоп-листов сети ресторанов

Позволяет с помощью мобильного устройства оперативно просматривать блюда, поставленные на стоп, по списку ресторанов сети пиццерий без использования касс. Стоп-листы хранятся в базе PostgreSQL, автоматически обновляются каждые три часа библиотекой Celery. 

## Запуск 

make run 

## Стэк технологий

- Python
- Aiogram
- PostgreSQL
- SQLAlchemy
- Celery
- Redis
- Poetry
- Pylint
- Docker

## Примеры файлов окружений

- stop_lists_bot/db/.env

STOP_LIST_BOT_DB_IMAGE_NAME=stop_list_bot-db

STOP_LIST_BOT_DB_NAME=stop_list_bot

STOP_LIST_BOT_DB_USERNAME=stop_list_bot

STOP_LIST_BOT_DB_PASSWORD=stop_list_bot

STOP_LIST_BOT_DB_PORT=5432

STOP_LIST_BOT_DB_HOST=stop_list_bot-db

STOP_LIST_BOT_NETWORK="stop_list_bot"

- stop_lists_bot/.env

STOP_LIST_BOT_PROJECT_IMAGE_NAME=stop_list_bot-project

STOP_LIST_BOT_DB_IMAGE_NAME=stop_list_bot-db

STOP_LIST_BOT_DB_NAME=stop_list_bot

STOP_LIST_BOT_DB_USERNAME=stop_list_bot

STOP_LIST_BOT_DB_PASSWORD=stop_list_bot

STOP_LIST_BOT_DB_PORT=5432

STOP_LIST_BOT_DB_HOST=stop_list_bot-db

STOP_LIST_BOT_NETWORK="stop_list_bot"

STOP_LIST_BOT_CELERY_BROKER_URL="redis://redis:6379/1"

STOP_LIST_BOT_CELERY_RESULT_BACKEND="redis://redis:6379/1"

STOP_LIST_BOT_CELERY_BROKER_CONN_RETRY_ON_START=True

STOP_LIST_BOT_CELERY_TIMEZONE="Europe/Moscow"

STOP_LIST_BOT_CELERY_ENABLE_UTC=False

STOP_LIST_BOT_CELERY_TASK_TIME_LIMIT=43200

STOP_LIST_BOT_TELEGRAM_TOKEN="TELEGRAM_TOKEN"

STOP_LIST_BOT_IIKO_API_LOGIN="IIKO_API_LOGIN"
