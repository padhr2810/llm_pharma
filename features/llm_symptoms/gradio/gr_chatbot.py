import random
import gradio as gr

def alternatingly_agree(message, history):
    if len([h for h in history if h['role'] == "assistant"]) % 2 == 0:
        return f"Yes, I do think that '{message}'"
    else:
        return "I don't think so"

gr.ChatInterface(alternatingly_agree, type="messages").launch()