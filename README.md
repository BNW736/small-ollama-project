# 🌤️ Local AI Weather Agent

A full-stack AI application that combines real-time weather data with a local LLM (Llama 3 via Ollama) to provide intelligent, context-aware weather advice.

## 🚀 Tech Stack
* **Backend:** FastAPI (Python)
* **Database:** PostgreSQL
* **AI Engine:** Ollama (Llama 3 / Mistral)
* **Environment:** WSL (Linux)

## 🛠️ Setup & Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/BNW736/small-ollama-project.git](https://github.com/BNW736/small-ollama-project.git)
    cd small-ollama-project
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables**
    Create a `.env` file and add your keys:
    ```ini
    OPENWEATHER_API_KEY=your_key_here
    DATABASE_URL=postgresql://user:pass@localhost/dbname
    ```

4.  **Run the App**
    ```bash
    uvicorn app:app --reload
    ```
