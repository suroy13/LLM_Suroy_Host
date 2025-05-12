import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import openai  # Fixing OpenAI import

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key:
    api_key = api_key.strip()  # Ensuring no leading/trailing spaces

    if not api_key.startswith("sk-proj-"):
        print("An API key was found, but it doesn't start with 'sk-proj-'. Please check the key.")
    else:
        print("API key found and looks good so far!")
else:
    print("No API key was found! Please check the troubleshooting notebook.")

# Correct OpenAI Instantiation
openai.api_key = api_key

# Fixing typos in system prompt
systemPrompt = "You are an assistant that extracts the channel names from the given content name provided."

def userPrompt_Content(number):
    userPrompt = (
        f"You are an assistant that provides teh sqareroot of a number {number}"
        "Confirm with 'yes' if you understand the task."
    )
    return userPrompt
client = openai.OpenAI(api_key=api_key)
def messages_for(contentName):
    return [
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": userPrompt_Content(contentName)}
    ]

def summarize(name):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_for(name)
    )
    return response.choices[0].message.content

# Example call
print(summarize("2"))
