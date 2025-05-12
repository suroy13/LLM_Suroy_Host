import ollama
import requests
from bs4 import BeautifulSoup

MODEL = "llama3.2"


#Class to scrap Website
class webScrapingWebsite:

    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

ed = webScrapingWebsite("https://edwarddonner.com")
# print(ed.title)
# print(ed.text)

#----------------------
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def user_prompt_for(webScrapingWebsite):
    user_prompt = f"You are looking at a website titled {webScrapingWebsite.title}"
    user_prompt += "The contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too and extract it in a .txt file.\n\n"
    user_prompt += webScrapingWebsite.text
    return user_prompt

# See how this function creates exactly the format above

def messages_for(webScrapingWebsite):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(webScrapingWebsite)}
    ]

# And now: call the Ollama function instead of OpenAI

def summarize(url):
    website = webScrapingWebsite(url)
    messages = messages_for(website)
    response = ollama.chat(model=MODEL, messages=messages)
    return response['message']['content']

print(summarize("https://www.geeksforgeeks.org/difference-between-static-and-dynamic-web-pages/"))