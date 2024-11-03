
import gradio as gr

q = {
    "Age" : "What is your age?",
    "sex" : ["What is your sex?", ["Male", "Female"]],
    "Diagnoses" : "Do you have any medical diagnosis? Please list any diagnosis here",
    "Medication": "Do you take any medicines? Please list your medicines here."
}


import gradio as gr

with gr.Blocks() as demo:
    text_meds = gr.Textbox()
    text_diag = gr.Textbox()
    text_age  = gr.Textbox()
    choose_sex = gr.Dropdown(label="Sex", choices=["Male", "Female"])

demo.launch()


