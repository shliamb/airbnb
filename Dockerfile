FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# # Установка PostgreSQL и утилиты pg_dump и еще разной мути..
RUN apt-get update && apt-get install -y apt-utils \
    postgresql \
    postgresql-contrib \
    postgresql-client \
    wget \
    gnupg2 \
    unzip \
    libxss1 \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    fonts-liberation \
    xdg-utils \
    curl

RUN echo "deb http://deb.debian.org/debian/ bookworm main" >> /etc/apt/sources.list && \
    apt-get update && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Создаем shell-скрипт для запуска всех трех файлов
RUN echo '#!/bin/sh\n\
python app/bot.py &\n\
python app/parser_object.py &\n\
#python app/parser_list.py &\n\

wait' > start.sh && chmod +x start.sh

CMD ["./start.sh"]