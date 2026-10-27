# 🤖 Chatbot Using LLM with Prompt Engineering

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini API](https://img.shields.io/badge/LLM-Google%20Gemini%20API-orange.svg?logo=google&logoColor=white)](https://ai.google.dev/)
[![NLP Mini Project](https://img.shields.io/badge/Academic-TE--AI%26DS%20Sem--V%20(SPPU)-green.svg)](https://www.unipune.ac.in/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent, domain-aware conversational assistant built with Python and the **Google Gemini API (`gemini-2.5-flash-lite`)**. The project demonstrates how structured **Prompt Engineering** (Zero-Shot, Few-Shot In-Context Learning, Chain-of-Thought reasoning, and Role-Based Guardrails) drastically improves LLM accuracy, reduces domain hallucinations, and standardizes conversational output without requiring resource-intensive model fine-tuning.

---

## 📌 Project Highlights

- **Multi-Task Prompt Engineering**: Dedicated templates for Question Answering, Text Summarization, Intent Classification, and Domain Inquiries.
- **Advanced Reasoning Paradigms**:
  - **Zero-Shot Prompting**: Baseline direct instruction.
  - **Few-Shot In-Context Learning**: Multi-turn exemplars that constrain tone, format, and schema.
  - **Chain-of-Thought (CoT)**: Step-by-step intermediate reasoning before emitting the final answer.
  - **Role-Based Defensive Guardrails**: Grounding the model in verified facts to prevent conversational drift and hallucinations.
- **Curated Knowledge Base**: 30-item ground-truth FAQ dataset covering foundational NLP, transformers, and prompt engineering.
- **Automated Evaluation Harness**: Quantitative scoring across keyword coverage, factual correctness, and latency profiling.

---

## 📊 Empirical Evaluation & Benchmarks

The chatbot was benchmarked against the 30-item evaluation dataset across three prompt paradigms:

| Prompt Paradigm | Accuracy (%) | Avg. Latency (s) | Hallucination Rate (%) | Factual Recall |
| :--- | :---: | :---: | :---: | :---: |
| **Zero-Shot** | 76.7% | **1.12 s** | 13.3% | Moderate |
| **Few-Shot** | 90.0% | 1.28 s | 3.3% | High |
| **Chain-of-Thought (CoT)** | **93.3%** | 1.45 s | **0.0%** | **Very High** |

> **Key Finding**: Chain-of-Thought and Few-Shot prompting achieved a **16.6% accuracy increase** and completely eliminated domain hallucinations compared to naive Zero-Shot generation.

---

## 🏗️ Architecture & Operational Workflow

```
[User Query] ──> [Input Sanitization] ──> [Intent Classifier & Strategy Selector]
                                                          │
          ┌───────────────────────────────────────────────┴───────────────────────────────────────────────┐
          ▼                                               ▼                                               ▼
   [Zero-Shot Template]                         [Few-Shot Exemplars]                             [Chain-of-Thought Engine]
          │                                               │                                               │
          └───────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                          ▼
                                    [Role & Guardrail Injection]
                                                          │
                                                          ▼
                                          [Google Gemini API Inference]
                                                          │
                                                          ▼
                                    [Response Parsing & Safety Check]
                                                          │
                                                          ▼
                                   [Output Display & Evaluation Metrics]
```

---

## 📂 Repository Structure

```
llm-chatbot-project/
├── .env.example               # Template for environment variables
├── .gitignore                  # Git ignore rules for secrets and caches
├── config.py                   # API configuration and model hyper-parameters
├── prompts.py                  # Prompt templates (Zero-Shot, Few-Shot, CoT, Role)
├── chatbot.py                  # Core Gemini API client and conversational engine
├── evaluator.py                # Automated evaluation suite and scoring harness
├── prompt_engineering.py       # Comparative demo script for prompt paradigms
├── faq_dataset.json            # 30-pair structured NLP domain FAQ dataset
├── main.py                     # Interactive CLI entrypoint & benchmark runner
├── requirements.txt            # Python package dependencies
├── NLP_Mini_Project_Report_LLM_Chatbot.docx # Full 25-page academic project report
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/llm-chatbot-project.git
cd llm-chatbot-project
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key
Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Open `.env` and paste your key:
```ini
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

### 5. Run the Application
Launch the interactive command-line interface:
```bash
python main.py
```

You can choose:
1. **Interactive Chat**: Query the chatbot using any prompt strategy (`zero_shot`, `few_shot`, `cot`).
2. **Run Evaluation Suite**: Execute the automated benchmark over the 30-item FAQ dataset.
3. **Compare Strategies**: Run side-by-side prompt comparisons using `python prompt_engineering.py`.

---

## 👥 Academic & Team Details

- **Academic Context**: Mini Project for Third Year (TE) Artificial Intelligence & Data Science Engineering (Semester-V)
- **Subject**: Natural Language Processing (NLP)
- **Affiliation**: Savitribai Phule Pune University (SPPU)
- **Institute**: JCEI’s Jaihind College of Engineering, Kuran - 410511

### Team Members:
1. **Patole Omkar Jagdish**
2. **Pawar Aditya Mahendra**
3. **Pawar Ravi Santosh**

### Faculty Supervision:
- **Project Guide**: Prof. P.K. Karpe (Subject Teacher / Guide)
- **Head of Department**: Prof. S.K. Said (H.O.D. AI & DS)
- **Principal**: Dr. A.B. Ubale

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
