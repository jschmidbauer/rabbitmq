1. Create your virtual environment
<sub>python -m venv venv</sub>

2. Activate virtual environment
<sub>./venv/Scripts/Activate.ps1</sub>

3. Run docker compose to build and stand up rabbitmq container
<sub>cd ./docker</sub>
<sub>docker-compose up -d</sub>

4. Run python scripts ( producer to push items into the letterbox queue )
<sub>cd python </sub>
<sub>py producer.py</sub>

5. Login to containers management interface to see the queue
<sub>localhost:15672</sub>

6. Consume the message from rabbitmq
<sub>cd python</sub>
<sub>py consumer.py</sub>