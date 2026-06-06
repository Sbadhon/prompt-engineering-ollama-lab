import json

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from lessons.registry import LESSONS
from llm import create_llm


def parse_json_inputs(input_json: str) -> dict:
    if not input_json.strip():
        return {}

    try:
        parsed = json.loads(input_json)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON input: {error}") from error

    if not isinstance(parsed, dict):
        raise ValueError("Template inputs must be a JSON object.")

    return parsed


def render_lesson(lesson_name: str) -> str:
    lesson = LESSONS[lesson_name]

    return f"""
## {lesson_name}

### Definition
{lesson["definition"]}

### When to use
{lesson["when_to_use"]}

### Chain / Flow
`{lesson["flow"]}`

### Takeaway
{lesson["takeaway"]}

### Try next
{lesson["exercise"]}
""".strip()


def load_lesson(lesson_name: str):
    lesson = LESSONS[lesson_name]

    return (
        render_lesson(lesson_name),
        lesson["prompt"],
        json.dumps(lesson["inputs"], indent=2),
        "",
        "",
    )


def run_lesson(
    lesson_name: str,
    prompt_text: str,
    input_json: str,
    num_predict: int,
    temperature: float,
    top_p: float,
    top_k: int,
):
    lesson = LESSONS[lesson_name]
    llm = create_llm(num_predict, temperature, top_p, top_k)

    try:
        values = parse_json_inputs(input_json)

        if lesson["kind"] == "direct":
            formatted_prompt = prompt_text
            response = llm.invoke(formatted_prompt).content.strip()

        elif lesson["kind"] == "template":
            prompt_template = PromptTemplate.from_template(prompt_text)
            formatted_prompt = prompt_template.format(**values)
            response = llm.invoke(formatted_prompt).content.strip()

        elif lesson["kind"] == "runnable_lambda":
            prompt_template = PromptTemplate.from_template(prompt_text)

            def format_prompt(current_values: dict) -> str:
                return prompt_template.format(**current_values)

            chain = RunnableLambda(format_prompt) | llm | StrOutputParser()
            formatted_prompt = prompt_template.format(**values)
            response = chain.invoke(values).strip()

        elif lesson["kind"] == "lcel":
            prompt_template = PromptTemplate.from_template(prompt_text)
            chain = prompt_template | llm | StrOutputParser()
            formatted_prompt = prompt_template.format(**values)
            response = chain.invoke(values).strip()

        else:
            raise ValueError(f"Unsupported lesson kind: {lesson['kind']}")

        execution_details = f"""
### Executed Flow
`{lesson["flow"]}`

### Formatted Prompt
```text
{formatted_prompt}
```
""".strip()

        return execution_details, response

    except Exception as error:
        execution_details = "### Error"

        error_message = f"""
Something failed while running the lesson.

Common checks:
1. Make sure Ollama is running.
2. Make sure the model exists: `ollama list`
3. Make sure your JSON inputs match the placeholders in the prompt.
4. Make sure the selected lesson has the correct `kind`.

Error:
{error}
""".strip()

        return execution_details, error_message
