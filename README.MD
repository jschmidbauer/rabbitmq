1. Create your virtual environment
# python -m venv venv

2. Activate virtual environment
# ./venv/Scripts/Activate.ps1

3. Run docker compose to build and stand up rabbitmq container
# cd ./docker
# docker-compose up -d

4. Run python scripts ( producer to push items into the letterbox queue )
# cd python
# py producer.py

5. Login to containers management interface to see the queue
# localhost:15672

6. Consume the message from rabbitmq
# cd python
# py consumer.py