# Author : Subhankar Roy

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import json

# Load the API KEy for OpenAI
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if api_key.startswith("sk-proj-") and len(api_key) > 10:
    print("API key found and looks good so far!")
else:
    print("No API key was found ")
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key")
    print("An API key was found, but it looks like it might have space or tab characters at the start or end")

# Initialize OpenAI
MODEL= "gpt-4o-mini"
openai=OpenAI()

#Class to prepresent webpage that has been scraped and also listed out links in it 

class Website:
    """
    A utility class to represent a Website that we have scraped, now with links
    """
    def __init__(self, url):
        print("Fetching url")
        self.url = url
        responses=requests.get(url)
        self.body=responses.content
        soup=BeautifulSoup(self.body,'html.parser')
        self.title=soup.title.string if soup.title else "No title found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = "No body found"

        # Extract all links from the webpage
        links = [link.get('href') for link in soup.find_all('a')]
        self.links = [lnk for lnk in links if lnk]
        print("Links extracted")

    def get_contents(self):
        """
        Returns the contents of the website
        """
        return self.text 

ed=Website("https://learn.microsoft.com/en-us/")
# print(ed.links)   

# Prompting the model to summarize the website

system_prompt = "You are provided with a list of links found on a webpage. \
You are able to decide which of the links would be most relevant to include in a brochure about the company, \
such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
system_prompt += "You should respond in JSON as in this example:"
system_prompt += """
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page": "url": "https://another.full.url/careers"}
    ]
}
"""
# print(system_prompt)

# Function to create the user prompt

def user_prompt_for(website):
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt

# print(user_prompt_for(ed))

# Function to call the model    
def get_links(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_for(website)}
      ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)
    

# Call the function to get the links
huggingface = Website("https://huggingface.co")
print(huggingface.links)

