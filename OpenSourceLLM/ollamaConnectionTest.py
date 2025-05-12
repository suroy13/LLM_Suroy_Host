import requests
import ollama
# import os

# Load environment variables
MODEL= "llama3.2"

user_prompt = "Describe the current war situation between India and Palistan innot more than 250 words"
# Function to send a message to the Ollama model
messages = [{"role": "user", "content": user_prompt}]



response = ollama.chat(model=MODEL, messages=messages)
print(response['message']['content'])