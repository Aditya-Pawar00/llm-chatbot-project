"""
Configuration file for the LLM Chatbot project.
Stores API key and model settings.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================
# GEMINI API KEY
# Set your key in .env or as environment variable GEMINI_API_KEY
# Get your free key from: https://aistudio.google.com/apikey
# ============================================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Model to use (gemini-2.5-flash-lite is fast, efficient, and reliable)
MODEL_NAME = "gemini-2.5-flash-lite"

# Generation settings
MAX_OUTPUT_TOKENS = 1024
TEMPERATURE = 0.2  # Controls randomness (0.0 = deterministic, 1.0 = creative)
