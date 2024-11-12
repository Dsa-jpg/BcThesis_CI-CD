import os


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
UPLOAD_FOLDER = './app/uploads'

# Creates the upload folder if it does not already exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


