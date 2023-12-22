# FastAPI Application

This FastAPI application uses the Llama model to answer questions. It receives a list of messages and parameters for the Llama model, returning the model's response.

## Prerequisites

- Python 3.6 or higher
- FastAPI
- Uvicorn
- Llama-cpp-python
- OpenAI
- Pydantic

## Setup

1. **Clone repository and navigate to the project directory:**

    ```bash
    git clone <repository_url>
    cd llama_fastapi
    ```

2. **Activate virtual environment:**

    - On Windows:

    ```bash
    .\env\Scripts\activate
    ```

    - On Ubuntu:

    ```bash
    source env/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

**Start FastAPI server:**

```bash
uvicorn main:app --reload
