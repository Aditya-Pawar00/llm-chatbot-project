"""
prompt_engineering.py - Prompt Engineering Demonstration
=========================================================
This module demonstrates the improvement of responses using
different prompt engineering techniques:
  1. Zero-Shot Prompting  (no examples)
  2. Few-Shot Prompting   (with examples)
  3. Chain-of-Thought     (step-by-step reasoning)

It runs the same queries with all three techniques and compares results.
"""

import time


def demonstrate_prompt_engineering(chatbot):
    """
    Run a complete demonstration of prompt engineering techniques.
    Compares Zero-Shot, Few-Shot, and Chain-of-Thought prompting.

    Args:
        chatbot: An instance of the Chatbot class.
    """
    print("\n" + "=" * 70)
    print("🔬 PROMPT ENGINEERING DEMONSTRATION")
    print("    Comparing: Zero-Shot vs Few-Shot vs Chain-of-Thought")
    print("=" * 70)

    # ============================================================
    # DEMO 1: Q&A Task
    # ============================================================
    print("\n" + "─" * 70)
    print("📋 TASK 1: Question & Answering")
    print("─" * 70)

    qa_question = "What is the difference between Machine Learning and Deep Learning?"
    print(f"\nQuestion: {qa_question}\n")

    techniques = ["zero_shot", "few_shot", "chain_of_thought"]
    labels = ["🔵 Zero-Shot", "🟢 Few-Shot", "🟡 Chain-of-Thought"]

    for technique, label in zip(techniques, labels):
        print(f"\n{label}:")
        print("-" * 40)
        response = chatbot.answer_question(qa_question, prompt_type=technique)
        print(response)
        time.sleep(1)

    # ============================================================
    # DEMO 2: Summarization Task
    # ============================================================
    print("\n" + "─" * 70)
    print("📋 TASK 2: Text Summarization")
    print("─" * 70)

    sample_text = (
        "Artificial Neural Networks (ANNs) are computing systems inspired by biological neural "
        "networks in the human brain. They consist of interconnected nodes organized in layers: "
        "an input layer, one or more hidden layers, and an output layer. Each connection has a "
        "weight that adjusts during training. ANNs learn by processing training examples and "
        "adjusting weights to minimize prediction errors through a process called backpropagation. "
        "They are particularly effective for tasks like image recognition, speech processing, "
        "and natural language understanding. Modern deep neural networks with many hidden layers "
        "have achieved remarkable results in various fields including healthcare, autonomous "
        "driving, and scientific research."
    )
    print(f"\nOriginal Text ({len(sample_text.split())} words):")
    print(f"  \"{sample_text[:150]}...\"\n")

    for technique, label in zip(techniques, labels):
        print(f"\n{label}:")
        print("-" * 40)
        response = chatbot.summarize_text(sample_text, prompt_type=technique)
        print(response)
        time.sleep(1)

    # ============================================================
    # DEMO 3: Classification Task
    # ============================================================
    print("\n" + "─" * 70)
    print("📋 TASK 3: Text Classification")
    print("─" * 70)

    classification_texts = [
        "Scientists at CERN have detected a new subatomic particle that could change our understanding of physics.",
        "The latest smartphone features a 200MP camera and runs on a custom-designed chip.",
        "Drinking green tea daily has been linked to improved cardiovascular health and longevity.",
        "The university announced a new online degree program in artificial intelligence.",
    ]

    for text in classification_texts:
        print(f"\nText: \"{text}\"")
        print("-" * 40)
        for technique, label in zip(techniques, labels):
            response = chatbot.classify_text(text, prompt_type=technique)
            # Clean up the response to show just the category
            category = response.strip().split("\n")[0] if response else "Unknown"
            print(f"  {label}: {category}")
            time.sleep(0.5)

    # ============================================================
    # SUMMARY
    # ============================================================
    print("\n" + "=" * 70)
    print("📊 PROMPT ENGINEERING SUMMARY")
    print("=" * 70)
    print("""
┌─────────────────────┬──────────────────────────────────────────────┐
│ Technique           │ When to Use                                  │
├─────────────────────┼──────────────────────────────────────────────┤
│ 🔵 Zero-Shot        │ Simple tasks, general questions               │
│ 🟢 Few-Shot         │ When specific format/style is needed          │
│ 🟡 Chain-of-Thought │ Complex reasoning, multi-step problems        │
└─────────────────────┴──────────────────────────────────────────────┘

Key Observations:
  • Zero-Shot: Quick but may lack detail or specific formatting.
  • Few-Shot:  More structured output, follows the example pattern.
  • Chain-of-Thought: Most thorough, shows reasoning process.
    """)
    print("=" * 70)
