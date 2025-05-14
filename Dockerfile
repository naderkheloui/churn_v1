# Utilise une image Python officielle comme base
FROM python:3.12-slim

# Crée un répertoire pour l'application
WORKDIR /app

# Copie les fichiers nécessaires
COPY . /app

# Installe les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose le port sur lequel FastAPI va tourner
EXPOSE 8000

# Commande pour démarrer l'application en utilisant le port dynamique
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
