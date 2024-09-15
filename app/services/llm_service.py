import openai
from config import Config

# Load the API key from the config
openai.api_key = Config.OPENAI_API_KEY

def generate_summary(rolls, score):
    prompt = f"Provide a detailed summary of the bowling game where the player has rolled the following pins: {rolls}. The current score is {score}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes bowling games."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        summary = response['choices'][0]['message']['content'].strip()
        return summary
    except Exception as e:
        raise Exception(f"LLM service error: {str(e)}")
