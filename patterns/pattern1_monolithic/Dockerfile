# Dockerfile para el Patrón 1: Imagen monolítica
# Esta imagen contiene todos los modelos de IA y dependencias
FROM ros:humble

# Copiar código de la aplicación y modelos
COPY ./app /app

# Instalar dependencias de Python para los modelos
RUN apt-get update && apt-get install -y python3-pip \
    && pip3 install -r /app/requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Ejecutar el nodo principal de ROS 2
CMD ["ros2", "launch", "app", "monolithic_launch.py"]
