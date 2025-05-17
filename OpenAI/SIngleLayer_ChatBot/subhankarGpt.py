import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

class SubhankarGPT:
    """
    A class to represent the Subhankar GPT chat application.
    """
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = "gpt-4o-mini"
        self.openai = OpenAI()

        if self.api_key.startswith("sk-proj-"):
            print("API key found and looks good so far!")
        else:
            print("No API key found or invalid API key.")
            raise ValueError("Invalid API Key")
        
    def system_prompt(self):
        return "You are a very responsible AI chat bot that helps the users on asking questions \
                and provides accurate information. You should always be respectful and polite.\
                You are also a expert in programming and can help the user in coding specially in Selenium, Python, Java, C++, C#, JavaScript, HTML, CSS, and SQL."
    def user_prompt(self, USER_INPUT):
        return f"User: {USER_INPUT}"
    
  
    
    def get_response(self, USER_INPUT):
        """
        Get the response from OpenAI for the given user input.
        """
        completion = self.openai.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_prompt()},
                {"role": "user", "content": self.user_prompt(USER_INPUT)}
            ],
            model=self.model,
            temperature=0.3
        )
        return completion.choices[0].message.content   
        
     # Designing the UI
    def chatBOTUI(self):
        gr.Interface(
            fn=self.get_response,
            inputs=gr.Textbox(placeholder="Enter your message here..."),
            outputs=gr.Markdown(),
            title="Subhankar Single Layer Chat GPT",
            description=f"This is a single window chat application using OpenAI's {self.model} model.",
            allow_flagging="never",
        ).launch()
            
gpt=SubhankarGPT()
gpt.chatBOTUI()