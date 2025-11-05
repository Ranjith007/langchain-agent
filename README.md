# 🧠 LangChain-Agent: Modular AI Agent Framework

Welcome to **LangChain-Agent**, a fully customizable and extensible agent powered by LangChain, OpenAI LLMs, and dynamic tools. This project is built to help you explore, develop, and deploy real-world agentic applications using Python.

---

## 🚀 Features

- 🔁 **Dynamic Model Selection** — Automatically switches between base and advanced models based on conversation context.
- 🛠️ **Extensible Tooling System** — Pre-built tools for:
  - Web search (via SerpAPI)
  - Python code execution
  - File reading
  - Calculator
- 🧠 **Memory Support** — Includes conversation memory for agent continuity.
- 🧩 **Modular Architecture** — Easy to reorganize, understand, and extend.
- ⚡ Powered by `langchain` and `openai`.

---

## 📂 Project Structure

langchain-agent/
│
├── Tools/
│ ├── Tools_calculator.py # Math operations tool
│ ├── Tools_file_reader.py # File reading tool
│ ├── Tools_python_exec.py # Python code execution tool
│ └── Tools_web_search.py # Web search tool (SerpAPI)
│
├── memory/
│ └── memory_chat_memory.py # Memory handler for conversation persistence
│
├── middleware/
│ └── middleware_model_selector.py # Middleware for intelligent model routing
│
├── .env.example # Template for environment variables
├── .gitignore # Ignoring .env and other artifacts
├── agent_core.py # Agent initialization code
├── main.py # Project entry point
├── requirements.txt # Python dependencies
└── README.md # Documentation file





Setup Instructions

1. Clone the repository
     bash
   git clone https://github.com/Ranjith007/langchain-agent.git
   cd langchain-agent

2. Create a virtual environment
    python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
    pip install -r requirements.txt

4.Configure environment variables

    Copy .env.example → .env

    Add your OPENAI_API_KEY and SERPAPI_API_KEY in .env:

        OPENAI_API_KEY=your_openai_api_key_here
        SERPAPI_API_KEY=your_serpapi_api_key_here

5.Run the Agent

   python main.py



  How It Works
     The agent uses ChatOpenAI and integrates multiple tools.

    Conversation history is preserved using memory handlers.

    The middleware automatically selects the LLM model based on the length of the         conversation.

  Tech Stack

  | Component       | Library / API      |
| --------------- | ------------------ |
| Base LLM        | OpenAI GPT-4o-mini |
| Advanced LLM    | OpenAI GPT-4o      |
| Agent Framework | LangChain          |
| Web Search Tool | SerpAPI            |
| Memory          | LangChain Memory   |




