# Устанавка базового образ
FROM python:3.10-alpine

# Устанавка рабочего директория внутри контейнера
# Директорий будет создан если его не было
# Будет в дальнейшем использоваться как базовый
WORKDIR /app

# Копирование зависимостей
# Для того чтобы не пересобирать их каждый раз при сборке образа
COPY requirements.txt .

# Установка зависимостей
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Запуск тестов
CMD ["pytest"]
#так как одинекоторые из тестов выполняются очень долго (см. README) - для ускорения проверок эти тесты можно не выполнять
#при запуске образа рекомендется использовать набор команд pytest -n 4 -m "not slow"
#для образа с CMD ["pytest", "-m \"not slow\""]
#возникает ошибка: ERROR: Wrong expression passed to '-m':  "not slow": at column 2: unexpected character """