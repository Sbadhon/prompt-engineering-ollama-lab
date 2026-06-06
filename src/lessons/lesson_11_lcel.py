LESSON = {
    "title": "11 - LCEL Pattern",
    "kind": "lcel",
    "definition": "LCEL means LangChain Expression Language. It uses the pipe operator to connect steps.",
    "when_to_use": "Use it to build clear flows such as prompt -> model -> output parser.",
    "takeaway": "LCEL makes the data flow easy to read and extend.",
    "exercise": "Replace the content with your own study notes and summarize them.",
    "flow": "PromptTemplate -> ChatOllama -> StrOutputParser",
    "prompt": """
Summarize the following content in one sentence.

Content:
{content}

Summary:
""".strip(),
    "inputs": {
        "content": "Prompt engineering is the practice of designing clear instructions for language models. Good prompts define the task, context, constraints, and expected output format.",
    },
}
