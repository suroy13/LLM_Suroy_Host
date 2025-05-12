import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

if api_key.startswith("sk-proj-"):
    print("API key found and looks good so far!")
else:
    print("No API key found")

# Create instance of OpenAI
openai = OpenAI()
# Initialize the model
MODEL = "gpt-4o-mini"

class jokes:
    """
    A utility class to represent a Jokes
    """
    def __init__(self, jokesContent):
        self.jokesContent = jokesContent

choices=input("Please enter the type of jokes you want to hear: ")
jk=jokes(choices)        
        
        

#System Prompt

system_prompt = "You a helpful assistant. You should always be respectful and polite \
    to the user. You should always be honest and provide accurate information. \
        and if you don't know the answer, you should say 'I don't know'."
system_prompt += "You should be unbiased and not take sides."
system_prompt += "You should be concise and not provide unnecessary information."

# User Prompt
user_prompt = f"Act as a best comedian and provide jokes on the topic {jk.jokesContent}."
user_prompt += "Make sure it does not harm anyone's feelings and is not offensive or hurt any communal harmony."
user_prompt += "No jokes should be repeated. and not more than 3 jokes at a time"
user_prompt += "No Jokes on any Country, Religion, or Community. On this circumstances just Say 'I don't know'."

# Method  for messages in list of disctionaries
def messages_for():
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

# Function to get the response from OpenAI

def get_LLM_Response():

    response = openai.chat.completions.create(
        model = MODEL,
        messages = messages_for()
    )
    # Extract the content from the response
    result = response.choices[0].message.content
    return result

print(get_LLM_Response())

    

              