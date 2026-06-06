LESSON = {
    "title": "05 - Few-shot Prompt",
    "kind": "direct",
    "definition": "A few-shot prompt gives the model multiple examples before the real task.",
    "when_to_use": "Use it when labels, tone, structure, or formatting matter.",
    "takeaway": "Few-shot prompting usually improves consistency compared with zero-shot prompting.",
    "exercise": "Add examples for Anger and Surprise, then test another statement.",
    "flow": "Direct Prompt -> ChatOllama",
    "prompt": """
Classify the emotion in each statement.

Statement: "I just won my first marathon!"
Emotion: Joy

Statement: "I can't believe I lost my keys again."
Emotion: Frustration

Statement: "My best friend is moving to another country."
Emotion: Sadness

Statement: "That movie was so scary I had to cover my eyes."
Emotion:
""".strip(),
    "inputs": {},
}
