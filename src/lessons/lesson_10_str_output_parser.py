LESSON = {
    "title": "10 - StrOutputParser",
    "kind": "lcel",
    "definition": "StrOutputParser converts the model response into a plain string.",
    "when_to_use": "Use it at the end of a LangChain chain when you want clean text output.",
    "takeaway": "It keeps output simple and easy to display, test, or pass to another function.",
    "exercise": "Remove StrOutputParser in the code later and inspect the raw model response object.",
    "flow": "PromptTemplate -> ChatOllama -> StrOutputParser",
    "prompt": "Define {concept} in one simple paragraph.",
    "inputs": {
        "concept": "StrOutputParser",
    },
}
