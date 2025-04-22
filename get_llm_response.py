# Import Dependencies
import os
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

# ************************************************************ Groq Code ************************************************************

# Get the GROQ API key from the environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set the GROQ API Key in the environment
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

def get_llm_response(prompt: str) -> str:
    """
    Function to get the response from the LLM.
    :param prompt: The prompt to send to the LLM.
    :return: The response from the LLM.
    """
    # Get the response from the LLM
    response = llm.invoke(prompt)
    
    # Return the response text
    return response.content

# ****************************************************************************************************************
"""
LM Studio Test Code

import requests

def test_local_llm(prompt: str) -> str:
    "
    Function to test the local LLM API.
    :param prompt: The prompt to send to the LLM.
    :return: The response from the LLM.
    "
    # Set the URL for the local LLM API
    url = "http://localhost:1234/v1/completions"

    # Create a system prompt for the LLM
    # system_prompt = "You are a knowledgeable assistant."
    
    # Create the data payload with more parameters for better control
    data = {
        # "prompt": system_prompt + prompt,
        # "prompt": prompt,  # The prompt to send to the LLM
        "prompt": f"Q: {prompt}\nA:",  # Format as question-answer
        # "max_tokens": 100,
        "temperature": 0,
        "top_k": 40,  # Top-k sampling for diversity
        "RepetitionPenalty": 1.1,  # Penalty for repeated tokens
        "top_p": 0.95,
        "min_p": 0.05,
        "n": 1,
        "stop": ["\n"],  # Stop at new lines to get concise answers
        "echo": False,   # Don't echo the prompt in the response
    }
    
    try:
        # Send a POST request to the local LLM API
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        
        # Get the response JSON
        response_json = response.json()
        
        # Extract the generated text from the first choice
        if "choices" in response_json and len(response_json["choices"]) > 0:
            return response_json["choices"][0]["text"].strip()
        return "No response generated"
        
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


answer = test_local_llm("What is the capital of France?")
print(answer)
"""

# ********************************************************* OLLAMA Code *********************************************************

# No need for Ollama API key as it is not required for local models

lllm = ChatOllama(
    model="deepseek-r1:1.5b",
    # model="phi:latest",
    temperature=0,
)

def get_lllm_response(prompt: str) -> str:
    """
    Function to get the response from the LLM.
    :param prompt: The prompt to send to the LLM.
    :return: The response from the LLM.
    """
    modified_prompt = f"Q: {prompt}\nA:"  # Format as question-answer
    # Get the response from the LLM
    response = lllm.invoke(modified_prompt)
    
    # Return the response text
    return response.content

answer = get_lllm_response("What is the capital of France?")
print(answer)