#!/bin/bash

# Убедитесь, что вы запускаете этот скрипт из директории, где находится ваш docker-compose.yml

while true; do
    echo "Starting docker-compose up"
    docker-compose up #-d
    
    echo "Waiting for 30 minutes"
    sleep 1800  # Ждем 30 минут (1800 секунд)
    
    echo "Stopping docker-compose down"
    docker-compose down
    
    echo "Waiting for 3 minutes"
    sleep 180   # Ждем 3 минуты (180 секунд)
done