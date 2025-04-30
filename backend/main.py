from fastapi import FastAPI, Form, HTTPException
import requests

app = FastAPI()

@app.post("/review/")
def review_code(code: str = Form(...)):
    prompt = (
        "You are a senior developer. Please review the following code for bugs, improvements, "
        "and optimization tips:\n\n"
        f"{code}"
    )

    ollama_url = "http://localhost:11434/api/generate"
    payload = {"model": "deepseek-coder", "prompt": prompt, "stream": False}

    try:
        response = requests.post(ollama_url, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Error communicating with Ollama: {e}")

    try:
        result = response.json()
        review = result.get("response")
        if review is None:
            # Log the actual response from Ollama for debugging
            print(f"Unexpected Ollama response: {result}") 
            raise HTTPException(status_code=500, detail="Invalid response format from Ollama.")
        return {"review": review.strip()}
    except ValueError:
        raise HTTPException(status_code=500, detail="Error decoding Ollama response.")