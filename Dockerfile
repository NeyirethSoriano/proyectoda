FROM python:3.8-slim-buster

WORKDIR /app

# Actualizar paquetes del SO para parchear vulnerabilidades de OpenSSL
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]