# Import Dependencies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

# Import custom dependencies
from get_llm_response import get_llm_response

# Create FastAPI instance
app = FastAPI()

# CORS Middleware to allow requests from frontend
origins = ['*'] # Allow all origins for development purposes. Can be modified to restrict to specific domains in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins for development purposes
    allow_credentials=True, # Allows credentials (cookies, authorization headers, etc.)
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Input request pydantic data model
class InputRequest(BaseModel):
    question: str

# Output response pydantic data model
class OutputResponse(BaseModel):
    answer: str

# Define a post endpoint
@app.post("/ask", response_model=OutputResponse)
async def answer_question(input_request: InputRequest) -> OutputResponse:
    """
    Endpoint to handle question asking.
    :param input_request: Input request containing the question.
    :return: Output response containing the answer.
    """
    # Extract the question from the input request
    question = input_request.question
    answer = get_llm_response(question)  # Get the answer from the LLM
    # Return the answer in the output response model
    return OutputResponse(answer=answer)

# Only runs if you do python main.py
if __name__ == "__main__":
    # Run the FastAPI app using uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)