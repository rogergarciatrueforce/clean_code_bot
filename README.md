# 🧹 The Clean Code Bot (Automated Refactorer)

An AI-powered CLI tool that transforms "dirty" or undocumented Python code into optimized, **SOLID-compliant**, and fully documented code using Large Language Models (LLMs).

## 🎯 Project Goal
The main objective is to automate the refactoring process by applying **Clean Code** principles and generating comprehensive technical documentation (Docstrings/Type Hints) using a **Chain of Thought (CoT)** prompting strategy.

## 🛠️ Tech Stack
- **Language:** Python 3.12+
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (Extremely fast Python packager)
- **LLM Provider:** [Groq Cloud](https://console.groq.com/) (Llama-3.3-70b-versatile)
- **Libraries:** Click (CLI), Groq (API), Python-dotenv (Security)

## 🏗️ Project Structure
```text
clean_code_bot/
├── src/
│   └── bot.py           # Main CLI Script
├── examples/
│   ├── dirty_sample.py  # Code before refactoring
│   └── clean_sample.py  # Code after AI processing
├── .env.example         # Template for environment variables
├── requirements.txt     # Dependency list for replication
└── pyproject.toml       # Project configuration (uv)
```

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd clean_code_bot
   ```

2. **Install dependencies:**
   Since this project uses `uv`, you don't need to manually create a venv:
   ```bash
   uv sync
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```
   Add your Groq API Key:
   ```text
   GROQ_API_KEY=gsk_your_actual_key_here
   ```

## 💻 Usage
Run the bot against any Python file (e.g., the provided dirty sample):

```bash
uv run src/bot.py examples/dirty_sample.py
```

The optimized code will be saved in the `examples/` folder with a `clean_` prefix.

## 🔒 Security Features
- **Input Sanitization:** Validates file size and content before API calls.
- **Environment Protection:** Uses `.env` and `.gitignore` to prevent API key leaks.
- **Prompt Safety:** Structured system prompts to ensure the AI only performs code refactoring.

## 📄 License
MIT License - Free to use and modify.
