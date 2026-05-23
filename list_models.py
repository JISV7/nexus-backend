import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def list_available_models():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment or .env file.")
        return

    try:
        with genai.Client(api_key=api_key) as client:
            print(f"{'MODEL NAME':<40} | {'DISPLAY NAME'}")
            print("-" * 80)
            
            for model in client.models.list():
                print(f"{model.name:<40} | {model.display_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_available_models()
