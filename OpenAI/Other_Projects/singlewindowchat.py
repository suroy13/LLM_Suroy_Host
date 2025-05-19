import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

api_key=os.getenv('OPENAI_API_KEY')

MODEL="gpt-4o-mini"

openai=OpenAI()

system_prompt="You are a rude AI chat bot that mocks the users on asking questions"
user_prompt="Hello, GPT! This is my first ever message to you! Hi!"



def message_gpt(user_prompt):
    
    completion = openai.chat.completions.create(
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
        model=MODEL
        
    )
    return completion.choices[0].message.content


def sout(text):
    return text.upper()

# UI 

view =gr.Interface(
    fn=message_gpt,
    inputs=gr.Textbox(placeholder="Enter your message here..."),
    outputs=gr.Textbox(),
    title="Subhankar GPT",
    description="This is a single window chat application using OpenAI's GPT-4o-mini model.",
    theme="default",
    allow_flagging="never",
)

view.launch()