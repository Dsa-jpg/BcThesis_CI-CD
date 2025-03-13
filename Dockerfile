# Používáme oficiální Python obraz
FROM python:3.10-slim-buster

# Nastavíme pracovní adresář
WORKDIR /app

# Zkopírujeme požadavky a nainstalujeme závislosti
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080
# Zkopírujeme zbytek aplikace
COPY . .

# Spustíme aplikaci
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
