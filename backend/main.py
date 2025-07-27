from fastapi import FastAPI
from pydantic import BaseModel
from llm_handler import ask_llm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser les requêtes du frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    query: str

@app.post("/chat")
async def chat_endpoint(prompt: Prompt):
    response = ask_llm(prompt.query)
    return {"response": response}
