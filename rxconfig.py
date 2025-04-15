# import reflex as rx
# from decouple import config
# from dotenv import load_dotenv
# load_dotenv()
# print("dotenv is loaded",load_dotenv())

# DATABASE_URL = config("DATABASE_URL")
# config = rx.Config(
#     app_name="my_app",
    
#     db_url=DATABASE_URL
# )
# print(DATABASE_URL)

# import reflex as rx
# from decouple import config
# from dotenv import load_dotenv
# import os

# # Load .env from current directory explicitly
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# load_dotenv(dotenv_path=dotenv_path)

# # Verify loading
# print("Environment variables loaded:", os.getenv('DATABASE_URL') is not None)

# # Get DATABASE_URL with fallback for development
# DATABASE_URL = config("DATABASE_URL", default="sqlite:///reflex.db")  # Add default

# config = rx.Config(
#     app_name="my_app",
#     db_url=DATABASE_URL
# )

# print("Final DATABASE_URL:", DATABASE_URL)

import reflex as rx
import os

# Get DATABASE_URL with production-ready configuration
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    default="sqlite:///reflex.db"  # Fallback for local development
)

# Production validation
if os.environ.get("REFLEX_ENV_MODE") == "prod" and not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set in production environment")

config = rx.Config(
    app_name="my_app",
    db_url=DATABASE_URL
)

# Debug output
print("Database configuration loaded:")
print(f"Using DATABASE_URL: {DATABASE_URL}")
print(f"Environment mode: {os.environ.get('REFLEX_ENV_MODE', 'development')}")