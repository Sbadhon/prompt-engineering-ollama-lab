LESSON = {
    "title": "04 - One-shot Prompt",
    "kind": "direct",
    "definition": "A one-shot prompt gives the model one example before the real task.",
    "when_to_use": "Use it when you want to demonstrate the expected format or style.",
    "takeaway": "One example can make the output more predictable.",
    "exercise": "Change the target language from French to Spanish and update the example.",
    "flow": "Direct Prompt -> ChatOllama",
    "prompt": """
Example:

English: "How is the weather today?"
French: "Comment est le temps aujourd'hui?"

Now translate:

English: "Where is the nearest supermarket?"
French:
""".strip(),
    "inputs": {},
}
