# Используйте официальный образ Python
FROM python:3.11

RUN apt-get update && apt-get install -y wget && \
    wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz && \
    rm dockerize-linux-amd64-v0.6.1.tar.gz

# Установите рабочую директорию в контейнере
WORKDIR /usr/src/app

# Скопируйте файлы зависимостей
COPY requirements.txt ./

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте код вашего проекта в контейнер
COPY . .

# Укажите команду для запуска сервера
CMD ["dockerize", "-wait", "tcp://db:5432", "-timeout", "30s", "python", "manage.py", "runserver", "0.0.0.0:8000"]
