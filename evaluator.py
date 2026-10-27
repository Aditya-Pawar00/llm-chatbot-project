"""
evaluator.py - Response Quality Evaluation Module
====================================================
This module evaluates the quality and consistency of LLM responses.
It provides:
  - Response quality scoring (relevance, clarity, completeness)
  - Consistency checking (run same query multiple times)
  - Evaluation report generation
"""

import time


class ResponseEvaluator:
    """Evaluates the quality and consistency of chatbot responses."""

    def __init__(self, chatbot):
        """
        Initialize the evaluator with a chatbot instance.

        Args:
            chatbot: An instance of the Chatbot class.
        """
        self.chatbot = chatbot

    # ============================================================
    # 1. QUALITY EVALUATION using the LLM itself as a judge
    # ============================================================

    def evaluate_quality(self, question, response):
        """
        Evaluate the quality of a response using the LLM as a judge.
        Scores: Relevance, Clarity, Completeness (each out of 10).

        Args:
            question (str): The original question.
            response (str): The model's response to evaluate.

        Returns:
            dict: Evaluation scores and feedback.
        """
        eval_prompt = f"""You are an expert evaluator. Rate the following response on three criteria.
Give a score from 1-10 for each and a brief explanation.

Question: {question}

Response to evaluate: {response}

Evaluate on:
1. Relevance (1-10): How relevant is the response to the question?
2. Clarity (1-10): How clear and easy to understand is the response?
3. Completeness (1-10): How complete and thorough is the response?

Format your answer EXACTLY like this:
Relevance: [score]/10 - [brief explanation]
Clarity: [score]/10 - [brief explanation]
Completeness: [score]/10 - [brief explanation]
Overall: [average score]/10"""

        eval_response = self.chatbot.generate_response(eval_prompt, temperature=0.1)

        # Parse scores from response
        scores = self._parse_scores(eval_response)
        scores["raw_evaluation"] = eval_response

        return scores

    def _parse_scores(self, eval_text):
        """Parse numerical scores from the evaluation text."""
        scores = {
            "relevance": 0,
            "clarity": 0,
            "completeness": 0,
            "overall": 0,
        }

        for line in eval_text.split("\n"):
            line_lower = line.lower().strip()
            for key in scores:
                if line_lower.startswith(key):
                    # Extract the number after the colon
                    try:
                        # Find the score pattern like "8/10"
                        parts = line.split(":")
                        if len(parts) >= 2:
                            score_text = parts[1].strip()
                            score = int(score_text.split("/")[0].strip())
                            scores[key] = min(max(score, 0), 10)  # Clamp 0-10
                    except (ValueError, IndexError):
                        pass

        # Calculate overall if not parsed
        if scores["overall"] == 0 and any(scores[k] > 0 for k in ["relevance", "clarity", "completeness"]):
            non_zero = [scores[k] for k in ["relevance", "clarity", "completeness"] if scores[k] > 0]
            scores["overall"] = round(sum(non_zero) / len(non_zero), 1)

        return scores

    # ============================================================
    # 2. CONSISTENCY CHECK (run same query multiple times)
    # ============================================================

    def check_consistency(self, question, num_runs=3):
        """
        Check response consistency by running the same query multiple times.

        Args:
            question (str): The question to test.
            num_runs (int): Number of times to run the query.

        Returns:
            dict: Consistency analysis results.
        """
        print(f"\n🔄 Running consistency check ({num_runs} runs)...")
        responses = []

        for i in range(num_runs):
            print(f"   Run {i + 1}/{num_runs}...", end=" ", flush=True)
            response = self.chatbot.answer_question(question, prompt_type="zero_shot")
            responses.append(response)
            print("Done ✓")
            if i < num_runs - 1:
                time.sleep(1)  # Small delay between requests

        # Analyze consistency using the LLM
        consistency_prompt = f"""Analyze the consistency of these {num_runs} responses to the same question.

Question: {question}

{"".join(f'Response {i+1}: {r}' + chr(10) + chr(10) for i, r in enumerate(responses))}

Rate the consistency on a scale of 1-10 and explain:
- Are the key facts consistent across responses?
- Are there any contradictions?
- Do the responses vary only in wording or also in content?

Consistency Score: [score]/10
Analysis:"""

        analysis = self.chatbot.generate_response(consistency_prompt, temperature=0.1)

        return {
            "question": question,
            "num_runs": num_runs,
            "responses": responses,
            "consistency_analysis": analysis,
        }

    # ============================================================
    # 3. COMPREHENSIVE EVALUATION REPORT
    # ============================================================

    def generate_report(self, test_questions=None):
        """
        Generate a comprehensive evaluation report.

        Args:
            test_questions (list): List of questions to test. Uses defaults if None.

        Returns:
            str: Formatted evaluation report.
        """
        if test_questions is None:
            test_questions = [
                "What is Machine Learning?",
                "Explain the difference between AI and Machine Learning.",
                "What are the applications of Natural Language Processing?",
            ]

        report = []
        report.append("=" * 60)
        report.append("📊 CHATBOT EVALUATION REPORT")
        report.append("=" * 60)

        total_relevance = 0
        total_clarity = 0
        total_completeness = 0
        count = 0

        for i, question in enumerate(test_questions, 1):
            report.append(f"\n📝 Test {i}: {question}")
            report.append("-" * 50)

            # Get response
            response = self.chatbot.answer_question(question, prompt_type="few_shot")
            report.append(f"Response: {response[:200]}...")

            # Evaluate quality
            scores = self.evaluate_quality(question, response)
            report.append(f"\nScores:")
            report.append(f"  Relevance:    {scores['relevance']}/10")
            report.append(f"  Clarity:      {scores['clarity']}/10")
            report.append(f"  Completeness: {scores['completeness']}/10")
            report.append(f"  Overall:      {scores['overall']}/10")

            total_relevance += scores["relevance"]
            total_clarity += scores["clarity"]
            total_completeness += scores["completeness"]
            count += 1

        # Summary
        report.append("\n" + "=" * 60)
        report.append("📈 SUMMARY")
        report.append("=" * 60)

        if count > 0:
            report.append(f"  Questions tested:     {count}")
            report.append(f"  Avg Relevance:        {total_relevance / count:.1f}/10")
            report.append(f"  Avg Clarity:          {total_clarity / count:.1f}/10")
            report.append(f"  Avg Completeness:     {total_completeness / count:.1f}/10")
            avg_overall = (total_relevance + total_clarity + total_completeness) / (count * 3)
            report.append(f"  Avg Overall:          {avg_overall:.1f}/10")
        report.append("=" * 60)

        return "\n".join(report)
