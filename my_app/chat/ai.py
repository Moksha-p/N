
# import os
# from dotenv import load_dotenv , find_dotenv , dotenv_values
# from openai import OpenAI

# # Load environment variables from .env file
# # load_dotenv()

# # # ✅ Explicitly load .env file
# # dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
# # load_dotenv(dotenv_path)
# print("Current Working Directory:", os.getcwd())

# print("find_dotenv() found:", find_dotenv())
# dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',  '.env'))

# print("Looking for .env at:", dotenv_path)
# env_values = dotenv_values(dotenv_path)
# print(env_values) 
# OPEN_API_KEY = env_values.get("OPENAI_API_KEY")
# load_dotenv(dotenv_path=dotenv_path)
# print("DEBUG - OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# # # ✅ Debugging (REMOVE later)
# # print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
# # print("DATABASE_URL:", os.getenv("DATABASE_URL"))

# # Retrieve the API key
# OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# # Debugging: Print the key to check if it's being loaded
# if not OPEN_API_KEY:
#     raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")


# # Initialize OpenAI client with the correct API key
# client = OpenAI(api_key=OPEN_API_KEY)

# def get__llm_response(gpt_messages):
#     """Fetch response from OpenAI GPT model."""
#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",  
#         messages=gpt_messages
#     )

#     return completion.choices[0].message.content

# # Test environment variable loading
# print("OPENAI_API_KEY is set:", bool(OPEN_API_KEY))

import os
from dotenv import load_dotenv, find_dotenv, dotenv_values
from openai import OpenAI

# Print the current working directory for debugging
print("Current Working Directory:", os.getcwd())

# Check where find_dotenv() is finding the .env file
print("find_dotenv() found:", find_dotenv())

# Set the path to the .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Print the path of the .env file
print("Looking for .env at:", dotenv_path)

# Load environment variables from .env file
env_values = dotenv_values(dotenv_path)

# Print the loaded values from .env file to verify correct loading
print("Loaded env values:", env_values)

# Access OPENAI_API_KEY directly from env_values
OPEN_API_KEY = env_values.get("OPENAI_API_KEY")

# Check if the OPENAI_API_KEY is loaded correctly
if not OPEN_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# Print for debugging
print("OPENAI_API_KEY is set:", bool(OPEN_API_KEY))

# Initialize OpenAI client with the correct API key
client = OpenAI(api_key=OPEN_API_KEY)

def get_llm_response(gpt_messages):
    """Fetch response from OpenAI GPT model."""
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Use your desired model
        messages=gpt_messages
    )

    return completion.choices[0].message.content

# Test environment variable loading
print("OPENAI_API_KEY is set:", bool(OPEN_API_KEY))
