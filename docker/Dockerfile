# Use an official RabbitMQ image as the base image
FROM rabbitmq:3-management

# Expose all RabbitMQ ports
EXPOSE 4369
EXPOSE 5671
EXPOSE 5672
EXPOSE 15671
EXPOSE 15672
EXPOSE 15691
EXPOSE 15692
EXPOSE 25672

# Set the container name
ENV CONTAINER_NAME rabbitmq

# Set the hostname
ENV HOSTNAME rabbitmq

# Optional: Set environment variables if needed
# ENV RABBITMQ_USER=myuser
# ENV RABBITMQ_PASSWORD=mypassword

# Start RabbitMQ server
CMD ["rabbitmq-server"]
