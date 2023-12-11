# from fastapi import FastAPI
# from llama_cpp import Llama
# from pydantic import BaseModel, Field
# from typing import List, Dict, Optional

# app = FastAPI()

# class Message(BaseModel):
#     role: str
#     content: str

# class Params(BaseModel):
#     max_tokens: int
#     messages: List[Message]
#     top_p: Optional[float] = Field(None, ge=0, le=1)
#     top_k: Optional[int] = Field(None, ge=0)

# llm = Llama(model_path="mistral-7b-instruct-v0.1.Q8_0.gguf", chat_format="llama-2")

# @app.post("/answer")
# async def answer_question(params: Params):
#     output = llm.create_chat_completion(
#       max_tokens=params.max_tokens, 
#       messages=[{"role": msg.role, "content": msg.content} for msg in params.messages],
#       top_p=params.top_p,
#       top_k=params.top_k
#     )
#     return {"answer": output}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from llama_cpp import Llama
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class Params(BaseModel):
    max_tokens: Optional[int]
    messages: List[Message]
    top_p: Optional[float] = Field(None, ge=0, le=1)
    top_k: Optional[int] = Field(None, ge=0)

llm = Llama(model_path="mistral-7b-instruct-v0.1.Q8_0.gguf", chat_format="llama-2")

@app.post("/answer")
async def answer_question(params: Params):
    output = llm.create_chat_completion(
      max_tokens=params.max_tokens, 
      messages=[{"role": msg.role, "content": msg.content} for msg in params.messages],
      top_p=params.top_p,
      top_k=params.top_k
    )
    return {"answer": output}

