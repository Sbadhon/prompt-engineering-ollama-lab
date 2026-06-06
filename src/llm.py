import os

from langchain_ollama import ChatOllama


MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3.2:3b")


def create_llm(num_predict, temperature, top_p, top_k):
    return ChatOllama(
        model=MODEL_NAME,
        num_predict=int(num_predict),
        temperature=float(temperature),
        top_p=float(top_p),
        top_k=int(top_k),
    )
