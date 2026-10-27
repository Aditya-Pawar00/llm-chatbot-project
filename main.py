"""
main.py - Main Interactive Chatbot Application
================================================
This is the entry point of the project. It provides a menu-driven
interface to access all features:
  1. Q&A Chatbot
  2. Text Summarization
  3. Text Classification
  4. FAQ-Based Q&A
  5. Prompt Engineering Demo
  6. Evaluate Chatbot
  7. Consistency Check
"""

import sys
from chatbot import Chatbot
from evaluator import ResponseEvaluator
from prompt_engineering import demonstrate_prompt_engineering


def print_banner():
    """Print the welcome banner."""
    print("\n" + "=" * 60)
    print("  🤖 LLM CHATBOT with PROMPT ENGINEERING")
    print("  Mini Project - Built with Google Gemini API")
    print("=" * 60)


def print_menu():
    """Print the main menu."""
    print("\n┌────────────────────────────────────────┐")
    print("│           📋 MAIN MENU                 │")
    print("├────────────────────────────────────────┤")
    print("│  1. 💬 Q&A Chatbot                     │")
    print("│  2. 📝 Text Summarization               │")
    print("│  3. 🏷️  Text Classification              │")
    print("│  4. 📚 FAQ-Based Q&A                    │")
    print("│  5. 🔬 Prompt Engineering Demo          │")
    print("│  6. 📊 Evaluate Chatbot                 │")
    print("│  7. 🔄 Consistency Check                │")
    print("│  0. 🚪 Exit                             │")
    print("└────────────────────────────────────────┘")


def choose_prompt_type():
    """Let user choose the prompt engineering technique."""
    print("\n  Choose prompt technique:")
    print("    1. Zero-Shot (no examples)")
    print("    2. Few-Shot (with examples)")
    print("    3. Chain-of-Thought (step-by-step)")
    choice = input("  Your choice (1/2/3): ").strip()
    types = {"1": "zero_shot", "2": "few_shot", "3": "chain_of_thought"}
    return types.get(choice, "zero_shot")


def qa_mode(chatbot):
    """Interactive Q&A mode."""
    print("\n💬 Q&A Mode (type 'back' to return to menu)")
    prompt_type = choose_prompt_type()
    print(f"  Using: {prompt_type.replace('_', ' ').title()} prompting\n")

    while True:
        question = input("\n❓ Your question: ").strip()
        if question.lower() == "back":
            break
        if not question:
            continue

        print("\n🤔 Thinking...\n")
        response = chatbot.answer_question(question, prompt_type=prompt_type)
        print(f"🤖 Answer: {response}")


def summarization_mode(chatbot):
    """Interactive summarization mode."""
    print("\n📝 Summarization Mode (type 'back' to return to menu)")
    prompt_type = choose_prompt_type()
    print(f"  Using: {prompt_type.replace('_', ' ').title()} prompting\n")

    while True:
        print("\n📄 Enter text to summarize (or 'back' to return):")
        text = input().strip()
        if text.lower() == "back":
            break
        if not text:
            continue

        print("\n🤔 Summarizing...\n")
        response = chatbot.summarize_text(text, prompt_type=prompt_type)
        print(f"📋 Summary: {response}")


def classification_mode(chatbot):
    """Interactive classification mode."""
    print("\n🏷️ Classification Mode (type 'back' to return to menu)")
    print("  Categories: Technology, Science, Health, Education, Business, Sports, Entertainment")
    prompt_type = choose_prompt_type()
    print(f"  Using: {prompt_type.replace('_', ' ').title()} prompting\n")

    while True:
        print("\n📄 Enter text to classify (or 'back' to return):")
        text = input().strip()
        if text.lower() == "back":
            break
        if not text:
            continue

        print("\n🤔 Classifying...\n")
        response = chatbot.classify_text(text, prompt_type=prompt_type)
        print(f"🏷️ Classification: {response}")


def faq_mode(chatbot):
    """FAQ-based Q&A mode."""
    print("\n📚 FAQ Mode (type 'back' to return to menu)")
    print("  Ask questions about AI, ML, Deep Learning, NLP, etc.\n")

    while True:
        question = input("\n❓ Your question: ").strip()
        if question.lower() == "back":
            break
        if not question:
            continue

        print("\n🔍 Searching FAQ database...\n")
        response, match_count = chatbot.answer_from_faq(question)
        print(f"📊 Found {match_count} relevant FAQ entries")
        print(f"🤖 Answer: {response}")


def evaluation_mode(chatbot):
    """Run evaluation report."""
    print("\n📊 Generating Evaluation Report...")
    print("   This will test the chatbot with sample questions.\n")

    evaluator = ResponseEvaluator(chatbot)
    report = evaluator.generate_report()
    print(report)

    # Save report to file
    with open("evaluation_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("\n💾 Report saved to 'evaluation_report.txt'")


def consistency_mode(chatbot):
    """Run consistency check."""
    print("\n🔄 Consistency Check")
    question = input("❓ Enter a question to test: ").strip()
    if not question:
        question = "What is Machine Learning?"
        print(f"   Using default: '{question}'")

    evaluator = ResponseEvaluator(chatbot)
    results = consistency_check = evaluator.check_consistency(question, num_runs=3)

    print(f"\n{'='*50}")
    print(f"Question: {results['question']}")
    print(f"Runs: {results['num_runs']}")
    print(f"{'='*50}")

    for i, response in enumerate(results["responses"], 1):
        print(f"\n📝 Response {i}:")
        print(f"   {response[:200]}...")

    print(f"\n📊 Consistency Analysis:")
    print(results["consistency_analysis"])


def main():
    """Main function - entry point of the application."""
    print_banner()

    # Initialize the chatbot
    try:
        chatbot = Chatbot()
    except Exception as e:
        print(f"\n❌ Failed to initialize chatbot: {e}")
        print("   Make sure your API key is correct in config.py")
        sys.exit(1)

    # Main loop
    while True:
        print_menu()
        choice = input("\n👉 Enter your choice (0-7): ").strip()

        if choice == "1":
            qa_mode(chatbot)
        elif choice == "2":
            summarization_mode(chatbot)
        elif choice == "3":
            classification_mode(chatbot)
        elif choice == "4":
            faq_mode(chatbot)
        elif choice == "5":
            demonstrate_prompt_engineering(chatbot)
        elif choice == "6":
            evaluation_mode(chatbot)
        elif choice == "7":
            consistency_mode(chatbot)
        elif choice == "0":
            print("\n👋 Goodbye! Thanks for using the LLM Chatbot.")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 0-7.")


if __name__ == "__main__":
    main()
