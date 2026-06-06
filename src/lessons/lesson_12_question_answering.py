LESSON = {
    "title": "12 - Question Answering Chain",
    "kind": "lcel",
    "definition": "A question answering chain answers a question using provided context.",
    "when_to_use": "Use it when you want the model to stay grounded in specific text.",
    "takeaway": "This is the basic idea behind retrieval-augmented generation.",
    "exercise": "Ask a question that is not answered by the content and confirm the model says it is unsure.",
    "flow": "PromptTemplate -> ChatOllama -> StrOutputParser",
    "prompt": """
Answer the question based only on the provided content.
If the answer is not in the content, say "Unsure about the answer."

Content:
{content}

Question:
{question}

Answer:
""".strip(),
    "inputs": {
        "content": "The inner planets Mercury, Venus, Earth, and Mars are rocky planets.",
        "question": "Which planets are rocky?",
    },
}
