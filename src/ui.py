import gradio as gr

from lessons.registry import LESSONS
from llm import MODEL_NAME
from runner import load_lesson, run_lesson


def build_app():
    lesson_names = list(LESSONS.keys())

    with gr.Blocks(title="Prompt Engineering Learning Lab") as demo:
        gr.Markdown(
            f"""
# Prompt Engineering Learning Lab

Using local Ollama model: `{MODEL_NAME}`

Choose a lesson, review the definition, edit the prompt, tune the parameters, and run it.
""".strip()
        )

        with gr.Row():
            with gr.Column(scale=1):
                lesson_dropdown = gr.Dropdown(
                    choices=lesson_names,
                    value=lesson_names[0],
                    label="Lesson",
                )

                lesson_markdown = gr.Markdown()

                with gr.Accordion("Generation Parameters", open=True):
                    num_predict = gr.Slider(
                        minimum=32,
                        maximum=1024,
                        value=256,
                        step=32,
                        label="num_predict",
                    )
                    temperature = gr.Slider(
                        minimum=0.0,
                        maximum=1.5,
                        value=0.5,
                        step=0.1,
                        label="temperature",
                    )
                    top_p = gr.Slider(
                        minimum=0.1,
                        maximum=1.0,
                        value=0.8,
                        step=0.05,
                        label="top_p",
                    )
                    top_k = gr.Slider(
                        minimum=1,
                        maximum=100,
                        value=20,
                        step=1,
                        label="top_k",
                    )

            with gr.Column(scale=2):
                prompt_text = gr.Textbox(
                    label="Prompt / Template",
                    lines=12,
                )

                input_json = gr.Textbox(
                    label="Template Inputs JSON",
                    lines=8,
                )

                run_button = gr.Button("Run Lesson", variant="primary")

                execution_details = gr.Markdown()

                response_output = gr.Textbox(
                    label="Model Response",
                    lines=14,
                )

        lesson_dropdown.change(
            fn=load_lesson,
            inputs=[lesson_dropdown],
            outputs=[
                lesson_markdown,
                prompt_text,
                input_json,
                execution_details,
                response_output,
            ],
        )

        run_button.click(
            fn=run_lesson,
            inputs=[
                lesson_dropdown,
                prompt_text,
                input_json,
                num_predict,
                temperature,
                top_p,
                top_k,
            ],
            outputs=[execution_details, response_output],
        )

        demo.load(
            fn=load_lesson,
            inputs=[lesson_dropdown],
            outputs=[
                lesson_markdown,
                prompt_text,
                input_json,
                execution_details,
                response_output,
            ],
        )

    return demo
