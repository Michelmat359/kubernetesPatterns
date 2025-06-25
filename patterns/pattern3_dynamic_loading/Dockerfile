# Dockerfile para el Patrón 3: Carga dinámica de módulos
FROM ros:humble

# Instalar herramientas para descargar modelos en tiempo de ejecución
RUN apt-get update && apt-get install -y wget curl python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copiar la aplicación base sin modelos
COPY ./app /app

CMD ["ros2", "launch", "app", "dynamic_launch.py"]
