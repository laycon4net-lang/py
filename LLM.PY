import requests
from config import GROQ_API_KEY
from colorama import Fore, init

init(autoreset=True)

API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.1-8b-instant"


def summarize(text, max_tokens=150):

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": f"Summarize:\n{text}"}],
        "max_tokens": max_tokens,
        "temperature": 0.3
    }

    res = requests.post(API_URL, headers=headers, json=data).json()

    return res["choices"][0]["message"]["content"]



name = input("Your name: ") or "User"

text = input("\nEnter text: ")

if text:

    print(Fore.BLUE + "\nSummarizing...\n")

    result = summarize(text)

    print(Fore.GREEN + f"Summary for {name}:\n")

    print(result)

else:
    print("No text entered ❌")
