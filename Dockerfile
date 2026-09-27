FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos e instala as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da API
COPY . .

# Expõe a porta 5000 utilizada pelo Flask
EXPOSE 5000

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py

# Inicializa o servidor
CMD ["python", "app.py"]
