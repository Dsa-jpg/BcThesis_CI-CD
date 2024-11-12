from openai import OpenAI
from config import OPENAI_API_KEY

# Create OpenAI client instance for API calls
client = OpenAI(api_key=OPENAI_API_KEY)

def get_openai_response(prompt, user_message) :
    """
    This function sends a prompt and user message to `OpenAI API` and returns the response.
    
    :param prompt: The prompt to send to the API.
    :param user_message: The user's message to send to the API.

    :return: The response from the API as a string.
    
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content
