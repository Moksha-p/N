
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
# load_dotenv()

# ✅ Explicitly load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path)
# ✅ Debugging (REMOVE later)
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("DATABASE_URL:", os.getenv("DATABASE_URL"))

# Retrieve the API key
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# Debugging: Print the key to check if it's being loaded
if not OPEN_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")


# Initialize OpenAI client with the correct API key
client = OpenAI(api_key=OPEN_API_KEY)

def get__llm_response(gpt_messages):
    """Fetch response from OpenAI GPT model."""
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=gpt_messages
    )

    return completion.choices[0].message.content

# Test environment variable loading
print("OPENAI_API_KEY is set:", bool(OPEN_API_KEY))
