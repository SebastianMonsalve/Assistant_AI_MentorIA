import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(api_key=API_KEY, base_url="https://openrouter.ai/api/v1")

def generar(prompt):
    try:
        print("⌛Enviando")
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        print("✅Respuesta recibida")
        if hasattr(response, "choices") and len(response.choices) > 0:
            print(response.choices[0].message.content.strip())
            return response.choices[0].message.content.strip()
        else:
            return "❌Sin respuesta"

    except Exception as e:
        print(f"Error: {e}")
        return f"Error al llamar a la API: {str(e)}"
