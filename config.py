from dotenv import load_dotenv
import os

load_dotenv()  

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Ensure API keys are loaded
if not TAVILY_API_KEY or not GOOGLE_API_KEY:
    raise ValueError("API keys missing! Check your .env file.")
