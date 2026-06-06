LESSON = {
    "title": "08 - PromptTemplate",
    "kind": "template",
    "definition": "PromptTemplate creates reusable prompts with placeholders for changing values.",
    "when_to_use": "Use it when the prompt structure stays the same but the inputs change.",
    "takeaway": "PromptTemplate separates fixed prompt structure from dynamic input values.",
    "exercise": "Change adjective to professional and content to software engineers.",
    "flow": "PromptTemplate -> format values -> ChatOllama",
    "prompt": "Tell me a {adjective} joke about {content}.",
    "inputs": {
        "adjective": "funny",
        "content": "chickens",
    },
}
