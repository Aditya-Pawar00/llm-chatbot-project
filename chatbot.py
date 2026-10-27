"""
chatbot.py - Core Chatbot Engine
=================================
This module handles all communication with the Gemini API.
It provides functions to:
  - Initialize the API client
  - Send prompts and get responses
  - Load and search the FAQ dataset
  - Perform Q&A, Summarization, and Classification tasks
"""

import json
from google import genai
from google.genai import types
from config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE
from prompts import (
    QA_ZERO_SHOT, QA_FEW_SHOT, QA_CHAIN_OF_THOUGHT,
    SUMMARIZE_ZERO_SHOT, SUMMARIZE_FEW_SHOT, SUMMARIZE_CHAIN_OF_THOUGHT,
    CLASSIFY_ZERO_SHOT, CLASSIFY_FEW_SHOT, CLASSIFY_CHAIN_OF_THOUGHT,
    FAQ_PROMPT
)


class Chatbot:
    """Main chatbot class that interacts with the Gemini API."""

    def __init__(self):
        """Initialize the chatbot with Gemini API client and load FAQ data."""
        # Create the Gemini API client with our API key
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = MODEL_NAME
        self.faq_data = self._load_faq_dataset()
        print("✅ Chatbot initialized successfully!")
        print(f"   Model: {self.model}")
        print(f"   FAQ entries loaded: {len(self.faq_data)}")

    def _load_faq_dataset(self):
        """Load the FAQ dataset from JSON file."""
        try:
            with open("faq_dataset.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            return data["faqs"]
        except FileNotFoundError:
            print("⚠️  FAQ dataset not found. FAQ search won't work.")
            return []

    # ============================================================
    # CORE: Send a prompt to Gemini and get response
    # ============================================================

    def generate_response(self, prompt, temperature=None):
        """
        Send a prompt to the Gemini API and return the response text.

        Args:
            prompt (str): The prompt to send to the model.
            temperature (float): Controls randomness (0.0 to 1.0).

        Returns:
            str: The model's response text.
        """
        try:
            temp = temperature if temperature is not None else TEMPERATURE

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temp,
                    max_output_tokens=1024,
                ),
            )

            return response.text

        except Exception as e:
            return f"❌ Error generating response: {str(e)}"

    # ============================================================
    # TASK 1: Question & Answering
    # ============================================================

    def answer_question(self, question, prompt_type="zero_shot"):
        """
        Answer a question using the specified prompt type.

        Args:
            question (str): The user's question.
            prompt_type (str): "zero_shot", "few_shot", or "chain_of_thought"

        Returns:
            str: The model's answer.
        """
        prompt_templates = {
            "zero_shot": QA_ZERO_SHOT,
            "few_shot": QA_FEW_SHOT,
            "chain_of_thought": QA_CHAIN_OF_THOUGHT,
        }

        template = prompt_templates.get(prompt_type, QA_ZERO_SHOT)
        prompt = template.format(question=question)

        return self.generate_response(prompt)

    # ============================================================
    # TASK 2: Summarization
    # ============================================================

    def summarize_text(self, text, prompt_type="zero_shot"):
        """
        Summarize a given text using the specified prompt type.

        Args:
            text (str): The text to summarize.
            prompt_type (str): "zero_shot", "few_shot", or "chain_of_thought"

        Returns:
            str: The summarized text.
        """
        prompt_templates = {
            "zero_shot": SUMMARIZE_ZERO_SHOT,
            "few_shot": SUMMARIZE_FEW_SHOT,
            "chain_of_thought": SUMMARIZE_CHAIN_OF_THOUGHT,
        }

        template = prompt_templates.get(prompt_type, SUMMARIZE_ZERO_SHOT)
        prompt = template.format(text=text)

        return self.generate_response(prompt)

    # ============================================================
    # TASK 3: Text Classification
    # ============================================================

    def classify_text(self, text, prompt_type="zero_shot"):
        """
        Classify a text into a category using the specified prompt type.

        Args:
            text (str): The text to classify.
            prompt_type (str): "zero_shot", "few_shot", or "chain_of_thought"

        Returns:
            str: The predicted category.
        """
        prompt_templates = {
            "zero_shot": CLASSIFY_ZERO_SHOT,
            "few_shot": CLASSIFY_FEW_SHOT,
            "chain_of_thought": CLASSIFY_CHAIN_OF_THOUGHT,
        }

        template = prompt_templates.get(prompt_type, CLASSIFY_ZERO_SHOT)
        prompt = template.format(text=text)

        return self.generate_response(prompt)

    # ============================================================
    # TASK 4: FAQ-Based Q&A (uses dataset as context)
    # ============================================================

    def search_faq(self, question):
        """
        Search the FAQ dataset for relevant entries matching the question.

        Args:
            question (str): The user's question.

        Returns:
            list: List of matching FAQ entries.
        """
        question_lower = question.lower()
        matches = []

        for faq in self.faq_data:
            # Simple keyword matching
            faq_question_lower = faq["question"].lower()
            faq_answer_lower = faq["answer"].lower()

            # Check if any significant word from the query appears in the FAQ
            query_words = [w for w in question_lower.split() if len(w) > 3]
            for word in query_words:
                if word in faq_question_lower or word in faq_answer_lower:
                    matches.append(faq)
                    break

        return matches

    def answer_from_faq(self, question):
        """
        Answer a question using the FAQ dataset as context.

        Args:
            question (str): The user's question.

        Returns:
            tuple: (answer_text, matched_faqs_count)
        """
        # Search for relevant FAQs
        matched_faqs = self.search_faq(question)

        # Build context from matched FAQs
        if matched_faqs:
            context = "\n".join(
                f"Q: {faq['question']}\nA: {faq['answer']}"
                for faq in matched_faqs[:5]  # Limit to top 5 matches
            )
        else:
            context = "No relevant FAQ entries found."

        # Generate response using FAQ context
        prompt = FAQ_PROMPT.format(context=context, question=question)
        response = self.generate_response(prompt)

        return response, len(matched_faqs)
