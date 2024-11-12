import speech_recognition as sr

def recognize_speech(file_path):
    """
    Recognize speech from an audio file using free `Google Speech Recognition API`.

    Args:
        file_path (str): The path to the audio file.    
    """

    recognizer = sr.Recognizer() # Creating a recognizer object
    try:

        with sr.AudioFile(file_path) as source:
 
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='cs-CZ') # Recognizing the speech from the audio file in Czech language
            return text
        
    except sr.UnknownValueError:
        raise Exception("Neslyšel jsem tě, zkus to znovu.")
    except sr.RequestError as e:
        raise Exception(f"Google Speech Recognition request failed; {e}")
