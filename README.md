# Code Review Assistant using DeepSeek-Coder via Ollama

This project provides a simple web interface to get code reviews using the `deepseek-coder` large language model, served locally via Ollama. You can paste your code into the frontend, and the backend will query the Ollama model to provide feedback on potential bugs, improvements, and optimizations.

## Technologies Used

*   **Backend:** [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. Chosen for its speed, ease of use, and automatic documentation generation.
*   **Frontend:** [Streamlit](https://streamlit.io/) - An open-source app framework for Machine Learning and Data Science teams. Chosen for its simplicity in creating interactive web applications directly from Python scripts.
*   **LLM Serving:** [Ollama](https://ollama.ai/) - Allows running large language models locally. Chosen for making it easy to pull and serve models like `deepseek-coder`.
*   **LLM:** [DeepSeek-Coder](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) - A code-specialized large language model. Chosen for its focus on code understanding and generation tasks.
*   **HTTP Client:** [Requests](https://requests.readthedocs.io/en/latest/) - Standard library for making HTTP requests in Python. Used for communication between the frontend/backend and backend/Ollama.

## Getting Started

### Prerequisites

1.  **Python 3.7+:** Ensure you have Python installed.
2.  **Ollama:** Install Ollama from [ollama.ai](https://ollama.ai/) and ensure it's running.
3.  **Git:** Ensure you have Git installed.

### Step 1: Clone the Repository

Clone the project from GitHub:

    git clone https://github.com/ashish-kj/CodeReviewAssistant.git
    cd CodeReviewAssistant

### Step 2: Set Up Environment and Install Dependencies

Create a virtual environment and install the required Python packages:

    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    pip install -r requirements.txt

*(If `requirements.txt` is missing, you can create it after installing packages manually: `pip install fastapi uvicorn streamlit requests` then `pip freeze > requirements.txt`)*

### Step 3: Pull the DeepSeek-Coder Model via Ollama

Make sure the Ollama application or server is running, then pull the model:

    ollama pull deepseek-coder

### Step 4: Run the Backend (FastAPI)

Navigate to the backend directory (if not already there) and start the FastAPI server:

    # If you are in the root 'CodeReviewAssistant' directory:
    uvicorn backend.main:app --reload --port 8000

The backend API will be available at `http://localhost:8000`.

### Step 5: Run the Frontend (Streamlit)

Open a *new* terminal window/tab, activate the virtual environment again (`source venv/bin/activate` or `venv\Scripts\activate`), and run the Streamlit app:

    # If you are in the root 'CodeReviewAssistant' directory:
    streamlit run frontend/app.py

The frontend application will open in your web browser, usually at `http://localhost:8501`.

### Step 6: Use the App

Paste your code into the text area on the Streamlit app and click "Get Review" to receive feedback from the DeepSeek-Coder model.

## Project Structure

    CodeReviewAssistant/
    ├── backend/
    │   └── main.py       # FastAPI application
    ├── frontend/
    │   └── app.py        # Streamlit application
    ├── .gitignore        # Files to ignore for Git
    ├── LICENSE           # Project License
    ├── requirements.txt  # Python dependencies
    └── README.md         # This file