# Používáme oficiální Python obraz
FROM python:3.10-slim-buster

# Nastavíme pracovní adresář
WORKDIR /app

# Zkopírujeme požadavky a nainstalujeme závislosti
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Zkopírujeme zbytek aplikace
COPY . .

# Spustíme aplikaci
CMD ["python","app/main.py"]
