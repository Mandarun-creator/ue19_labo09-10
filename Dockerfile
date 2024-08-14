# Utilisez une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances
RUN pip install -r requirements.txt

# Exécuter l'application
CMD ["python", "app.py"]