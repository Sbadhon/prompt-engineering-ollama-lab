# Prompt Engineering Learning Lab with Ollama

A local Gradio web app for practicing prompt engineering with Ollama and LangChain.

The app lets you:

- choose a lesson
- read the definition
- review when to use the technique
- edit the prompt
- edit template input values
- tune model parameters
- run the prompt from the browser
- compare outputs

## Tech Stack

- Python 3.11
- Ollama
- llama3.2:3b
- Gradio
- LangChain Core
- langchain-ollama

## Project Structure

    prompt-engineering-ollama-lab/
    ├── src/
    │   ├── app.py
    │   ├── ui.py
    │   ├── llm.py
    │   ├── runner.py
    │   └── lessons/
    │       ├── __init__.py
    │       ├── registry.py
    │       ├── lesson_01_generation_parameters.py
    │       ├── lesson_02_basic_prompt.py
    │       ├── lesson_03_zero_shot.py
    │       ├── lesson_04_one_shot.py
    │       ├── lesson_05_few_shot.py
    │       ├── lesson_06_chain_of_thought.py
    │       ├── lesson_07_self_consistency.py
    │       ├── lesson_08_prompt_template.py
    │       ├── lesson_09_runnable_lambda.py
    │       ├── lesson_10_str_output_parser.py
    │       ├── lesson_11_lcel.py
    │       ├── lesson_12_question_answering.py
    │       └── lesson_13_product_review_analyzer.py
    ├── README.md
    ├── requirements.txt
    └── .gitignore

## Setup

Create and activate a virtual environment:

    python -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Pull the Ollama model:

    ollama pull llama3.2:3b

Run the app:

    python src/app.py

Open in browser:

    http://127.0.0.1:7860

## Lessons

| Lesson | Topic |
|---|---|
| 01 | Generation Parameters |
| 02 | Basic Prompt |
| 03 | Zero-shot Prompt |
| 04 | One-shot Prompt |
| 05 | Few-shot Prompt |
| 06 | Chain-of-thought Style Prompt |
| 07 | Self-consistency Prompt |
| 08 | PromptTemplate |
| 09 | RunnableLambda |
| 10 | StrOutputParser |
| 11 | LCEL Pattern |
| 12 | Question Answering Chain |
| 13 | Product Review Analyzer |

## How To Add a New Lesson

1. Create a new file inside `src/lessons`.
2. Add a `LESSON` dictionary.
3. Import it in `src/lessons/registry.py`.
4. Add it to `LESSON_LIST`.

Each lesson should include:

- title
- kind
- definition
- when_to_use
- takeaway
- exercise
- flow
- prompt
- inputs

## Lesson Kinds

The app supports these lesson kinds:

| Kind | Meaning |
|---|---|
| direct | Sends the prompt directly to Ollama |
| template | Uses PromptTemplate formatting |
| runnable_lambda | Uses RunnableLambda before the model |
| lcel | Uses PromptTemplate -> ChatOllama -> StrOutputParser |

## Recommended Learning Flow

1. Start the app.
2. Select a lesson.
3. Read the definition.
4. Run the default prompt.
5. Change the prompt.
6. Change the JSON inputs if the prompt has placeholders.
7. Change model parameters.
8. Re-run and compare the output.
9. Complete the exercise shown in the lesson.
