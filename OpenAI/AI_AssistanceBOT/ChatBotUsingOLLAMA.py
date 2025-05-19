# @author: Subhankar Roy
# This is a simple Gradio app that uses Ollama model to provide assistance.
# Importing necessary libraries

import ollama
import gradio as gr

MODEL= "gemma3:1b"

system_prompt = "You are a helpful assistant"


# Function to get the response from OLLAMA with historical context
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]

# Printing the history and messages for debugging
    print("History is:")
    print(history)
    print("And messages is:")
    print(messages)

# Streaming the response from OLLAMA LLM

    stream = ollama.chat(model=MODEL, messages=messages, stream=True)


    response = ""
    for chunk in stream:
        response += chunk.get("message", {}).get("content", "")
        yield response


# Initiating the UI compoments 
# custom_theme = gr.Theme(primary_color="black", background_fill="black")
gr.ChatInterface(fn=chat,title="Subhankar OLLAMA Assistance Chat BOT!", type="messages").launch()