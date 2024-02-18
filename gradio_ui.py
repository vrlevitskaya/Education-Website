import gradio as gr
from utils import return_generated_tasks

demo = gr.Interface(
    return_generated_tasks,
    inputs=[
        gr.Dataframe(
            label="Таблица с оценками",
            headers=["ФИО Ученика", "Предмет", "Тема", "Оценка"],
            datatype=["str", "str", "str", "number"],
            row_count=5,
            col_count=4,
        ),
        gr.Dropdown(
                    choices=[i for i in range(1, 12)],
                    label="Выберите класс обучения для учеников"
                    ),
        gr.Dropdown(
                    choices=[i for i in range(1, 5)],
                    label="Выберите курс обучения для студентов"
                    ),
    ],
    outputs="file",
    description="",
)

if __name__ == "__main__":
    demo.launch()

