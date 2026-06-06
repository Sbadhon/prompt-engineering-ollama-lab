LESSON = {
    "title": "09 - RunnableLambda",
    "kind": "runnable_lambda",
    "definition": "RunnableLambda wraps a normal Python function so it can be used inside a LangChain chain.",
    "when_to_use": "Use it when you need custom formatting or transformation logic before calling the model.",
    "takeaway": "RunnableLambda lets Python functions participate in LangChain pipelines.",
    "exercise": "Change the topic to PromptTemplate or LCEL.",
    "flow": "RunnableLambda(format_prompt) -> ChatOllama -> StrOutputParser",
    "prompt": "Explain {topic} to a beginner in two sentences.",
    "inputs": {
        "topic": "RunnableLambda",
    },
}
