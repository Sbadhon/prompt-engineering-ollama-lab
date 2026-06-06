LESSON = {
    "title": "07 - Self-consistency Prompt",
    "kind": "direct",
    "definition": "A self-consistency prompt asks the model to solve the same problem multiple ways and compare the results.",
    "when_to_use": "Use it when accuracy matters and the problem can be reasoned through more than one way.",
    "takeaway": "It helps identify a more reliable answer by checking whether multiple paths agree.",
    "exercise": "Try another age problem and check whether all explanations agree.",
    "flow": "Direct Prompt -> ChatOllama",
    "prompt": """
When I was 6, my sister was half my age. Now I am 70.

What age is my sister?

Provide three short independent explanations, then give the most consistent answer.
""".strip(),
    "inputs": {},
}
