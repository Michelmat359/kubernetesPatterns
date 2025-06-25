# Dockerfile para el Patrón 2: Microservicio de percepción
FROM ros:humble

# Copiar solo el modelo de IA correspondiente a este microservicio
COPY ./perception_model /app

RUN apt-get update && apt-get install -y python3-pip \
    && pip3 install -r /app/requirements.txt \
    && rm -rf /var/lib/apt/lists/*

CMD ["ros2", "run", "perception", "node"]
