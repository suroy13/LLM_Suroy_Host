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

class UC_BDD:
    """
    A utility class to Read Use Case from a .txt file
    """
    
        

#System Prompt

system_prompt = ""


# User Prompt
user_prompt = f""


# Method  for messages in list of disctionaries
def messages_for():
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

# Function to get the response from OpenAI

def get_LLM_Response():

    stream = openai.chat.completions.create(
        model = MODEL,
        messages = messages_for()
    )
    # Extract the content from the response
    result = stream.choices[0].message.content
    stream= True
    return result

print(get_LLM_Response())

    

              