import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Automatically loads .env from the current directory
 
def summarize_text(text_to_summarize):
    prompt = f"Please summarize the following text:\n\n{text_to_summarize}\n\nSummary:"
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    #print(client.api_key)

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100,
        temperature=0
        )
    print(response.choices[0].text) 
    #summary = response.choices[0].message['content'].strip()
    return response.choices[0].text

def sentiment_analyze(text_to_analyze):
    prompt = f"Analyze the sentiment of the following text: '{text_to_analyze}'. Classify it as positive, negative, or neutral."
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    #print(client.api_key)

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=10,
        temperature=0
        )

    print(response.choices[0].text) 
    #summary = response.choices[0].message['content'].strip()
    return response.choices[0].text
