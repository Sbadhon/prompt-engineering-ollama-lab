LESSON = {
    "title": "13 - Product Review Analyzer",
    "kind": "lcel",
    "definition": "This mini project combines prompt templates, structured instructions, LCEL, and output parsing.",
    "when_to_use": "Use this pattern for repeatable tasks like review analysis, ticket classification, or summarization.",
    "takeaway": "A strong prompt defines the task, input, constraints, and output format.",
    "exercise": "Add two more reviews and run them through the same chain.",
    "flow": "PromptTemplate -> ChatOllama -> StrOutputParser",
    "prompt": """
Analyze the product review.

Review:
{review}

Return the result in this exact format:
- Sentiment:
- Key Features Mentioned:
- Main Complaint:
- One Sentence Summary:
""".strip(),
    "inputs": {
        "review": "I love this smartphone. The camera quality is excellent and the battery lasts all day. The only issue is that it heats up during gaming.",
    },
}
