import gradio as gr
from utils import return_generated_tasks_docx



with gr.Blocks() as demo:
    gr.Markdown("Введите данные об учениках и нажмите кнопку 'Сгенерировать файл с заданиями', затем нажмите на файл "
                "'Задания', чтобы скачать его ")
    with gr.Row():
        inputs = [gr.Dataframe(

            label="Таблица с оценками",
            headers=["Номер", "ФИО Ученика", "Темы", "Предмет", "Количество заданий"],
            datatype=["number", "str", "str", "str", "number"],
            row_count=1,
            col_count=(5, 'fixed'),
        ),
            gr.Dropdown(
                choices=[i for i in range(1, 12)],
                label="Выберите класс обучения для учеников"
            )]
        outputs = gr.File()

    btn = gr.Button("Сгенерировать файл с заданиями")
    btn.click(fn=return_generated_tasks_docx, inputs=inputs, outputs=outputs)


demo.launch()

