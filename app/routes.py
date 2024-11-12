from flask import  Flask, Response, jsonify, request
from .openai_api import get_openai_response
from .prompt_generator import dynamic_prompt_generator, add_to_history, dynamic_prompt_json
from .speech_recognition_handler import recognize_speech
from .config import UPLOAD_FOLDER
import os


app = Flask('app', __name__)

@app.route('/response')
def get_response():
    try:
        prompt = dynamic_prompt_generator()
        response = get_openai_response(prompt, "Jak se mas a kolik je hodin a stupnu v CB?")
        return Response(response, mimetype="text/event-stream")
    except Exception as e:
        return Response(f"An error occured: {e}", status=500)
    

@app.route('/stats', methods=['GET'])
def get_stats():
    """
    Returns the statistics of the conversation history.

    """
    return jsonify(dynamic_prompt_json()), 200

@app.route('/upload-non-streamed', methods=['POST'])
def upload_file_non_streamed():
    """
    This endpoint is used to upload a file and get a response from the OpenAI API.

    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and (file.filename.endswith('.wav') or file.filename.endswith('.ogg')):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        try:
            text = recognize_speech(file_path)
            prompt = dynamic_prompt_generator()
            response = get_openai_response(prompt, text)

            add_to_history(text, response)

            return jsonify({'response': response}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400
