FROM python:3.13-slim

WORKDIR /app

# Actualizar paquetes del SO para parchear vulnerabilidades de OpenSSL
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "app:app"]