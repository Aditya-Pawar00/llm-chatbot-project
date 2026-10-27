"""
prompts.py - Prompt Templates for Different Tasks
==================================================
This module contains carefully designed prompt templates for:
  (a) Question & Answering (Q&A)
  (b) Text Summarization
  (c) Text Classification

Each task has multiple prompt versions to demonstrate prompt engineering:
  - Zero-Shot: No examples given
  - Few-Shot: A few examples provided
  - Chain-of-Thought: Step-by-step reasoning
"""


# ============================================================
# 1. QUESTION & ANSWERING PROMPTS
# ============================================================

QA_ZERO_SHOT = """You are a helpful AI assistant. Answer the following question clearly and concisely.

Question: {question}

Answer:"""


QA_FEW_SHOT = """You are a helpful AI assistant. Answer questions clearly and concisely.

Here are some examples:

Question: What is Python?
Answer: Python is a high-level, interpreted programming language known for its simple syntax and versatility. It is widely used in web development, data science, AI, and automation.

Question: What is an algorithm?
Answer: An algorithm is a step-by-step set of instructions designed to perform a specific task or solve a particular problem. It is a fundamental concept in computer science.

Now answer the following question in the same style:

Question: {question}

Answer:"""


QA_CHAIN_OF_THOUGHT = """You are a helpful AI assistant. Answer the following question by thinking step by step.

Question: {question}

Let me think through this step by step:
Step 1: Identify what the question is asking.
Step 2: Recall relevant knowledge about this topic.
Step 3: Formulate a clear, comprehensive answer.

Answer:"""


# ============================================================
# 2. SUMMARIZATION PROMPTS
# ============================================================

SUMMARIZE_ZERO_SHOT = """Summarize the following text in 2-3 concise sentences.

Text: {text}

Summary:"""


SUMMARIZE_FEW_SHOT = """Summarize texts concisely in 2-3 sentences. Here are some examples:

Text: "Machine learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention. Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision."
Summary: Machine learning automates data analysis using AI, enabling systems to learn from data and make decisions independently. It is widely applied in fields like medicine, email filtering, and computer vision.

Text: "Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services on an as-needed basis from a cloud provider."
Summary: Cloud computing provides IT resources over the internet with flexible pricing. It eliminates the need for physical infrastructure by offering on-demand access to technology services.

Now summarize the following text in the same style:

Text: {text}

Summary:"""


SUMMARIZE_CHAIN_OF_THOUGHT = """Summarize the following text by analyzing it step by step.

Text: {text}

Let me analyze this step by step:
Step 1: Identify the main topic of the text.
Step 2: Extract the key points and important details.
Step 3: Combine them into a concise 2-3 sentence summary.

Summary:"""


# ============================================================
# 3. CLASSIFICATION PROMPTS
# ============================================================

CLASSIFY_ZERO_SHOT = """Classify the following text into one of these categories: Technology, Science, Health, Education, Business, Sports, Entertainment.

Text: {text}

Category:"""


CLASSIFY_FEW_SHOT = """Classify texts into categories. Here are some examples:

Text: "Apple released the new iPhone with an improved camera and faster processor."
Category: Technology

Text: "Researchers discovered a new species of deep-sea fish in the Pacific Ocean."
Category: Science

Text: "Regular exercise and a balanced diet can reduce the risk of heart disease."
Category: Health

Text: "The stock market saw significant gains as tech companies reported strong earnings."
Category: Business

Now classify the following text:

Text: {text}

Category:"""


CLASSIFY_CHAIN_OF_THOUGHT = """Classify the following text into one of these categories: Technology, Science, Health, Education, Business, Sports, Entertainment.

Text: {text}

Let me think step by step:
Step 1: Read the text carefully and identify the main subject.
Step 2: Look for keywords that indicate the category.
Step 3: Match the subject to the most appropriate category.

Category:"""


# ============================================================
# 4. FAQ-BASED Q&A PROMPT (uses context from dataset)
# ============================================================

FAQ_PROMPT = """You are a helpful FAQ assistant. Use the provided FAQ context to answer the user's question.
If the answer is found in the FAQ context, provide it. If not, answer based on your general knowledge.

FAQ Context:
{context}

User Question: {question}

Answer:"""


# ============================================================
# HELPER: Get all prompt templates organized by task
# ============================================================

def get_all_prompts():
    """Returns a dictionary of all prompt templates organized by task and type."""
    return {
        "qa": {
            "zero_shot": QA_ZERO_SHOT,
            "few_shot": QA_FEW_SHOT,
            "chain_of_thought": QA_CHAIN_OF_THOUGHT,
        },
        "summarization": {
            "zero_shot": SUMMARIZE_ZERO_SHOT,
            "few_shot": SUMMARIZE_FEW_SHOT,
            "chain_of_thought": SUMMARIZE_CHAIN_OF_THOUGHT,
        },
        "classification": {
            "zero_shot": CLASSIFY_ZERO_SHOT,
            "few_shot": CLASSIFY_FEW_SHOT,
            "chain_of_thought": CLASSIFY_CHAIN_OF_THOUGHT,
        },
    }
