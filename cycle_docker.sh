#!/bin/bash
while true; do
    echo "Starting docker-compose up"
    # Запускаем docker-compose up в фоновом режиме
    docker-compose up &
    DOCKER_COMPOSE_PID=$!

    echo "Waiting for 30 minutes"
    sleep 1800  # Ждем 30 минут (1800 секунд)

    echo "Stopping docker-compose by sending SIGINT"
    kill -SIGINT $DOCKER_COMPOSE_PID

    # Ждем завершения процесса docker-compose
    wait $DOCKER_COMPOSE_PID

    echo "Stopping docker-compose down"
    docker-compose down
    
    echo "Waiting for 3 minutes"
    sleep 60   # Ждем 1 минуту (60 секунд)
done