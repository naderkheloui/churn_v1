# Utilise une image Python officielle comme base
FROM python:3.12-slim

#crée un repertoire pour l application
WORKDIR /app

#Copie les fichiers necessaires

COPY . /app

# Installe les dépendances

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose le port sur lequel FastAPI tourne
EXPOSE 8000

# Commande pour démmarer l'application
CMD ["uvicorn", "app.main.app", "--host", "0.0.0.0", "--port", "8000"]