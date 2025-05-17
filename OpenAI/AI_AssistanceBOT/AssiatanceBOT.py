# @author: Subhankar Roy
# This is a simple Gradio app that uses OpenAI's GPT-4o-mini model to provide assistance.
# Importing necessary libraries

import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

# Initialize
openai = OpenAI()
MODEL = 'gpt-4o-mini'

system_prompt = "You are a helpful assistant"


# Function to get the response from OpenAI with historical context
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] 
    + history 
    + [{"role": "user", "content": message}]

# Printing the history and messages for debugging
    print("History is:")
    print(history)
    print("And messages is:")
    print(messages)

# Streaming the response from OpenAI

    stream = openai.chat.completions.create(model=MODEL, messages=messages, temperature=0.7, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response


# Initiating the UI compoments 
gr.ChatInterface(fn=chat,title="Subhankar GPT Assistance!", type="messages").launch()
