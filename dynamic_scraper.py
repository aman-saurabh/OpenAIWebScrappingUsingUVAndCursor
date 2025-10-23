from scrapernew import fetch_website_contents
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load OpenAI API key
load_dotenv()
client = OpenAI()

def summarize_content(text: str) -> str:
    """Use OpenAI model to summarize webpage content."""
    prompt = f"Summarize this webpage content in 5 bullet points:\n\n{text[:6000]}"
    response = client.responses.create(model="gpt-4.1-mini", input=prompt)
    return response.output[0].content[0].text

def main():
    url = "https://openai.com"
    print(f"Scraping: {url}")

    html = fetch_website_contents(url)
    soup = BeautifulSoup(html, "html.parser")
    text = " ".join(s.strip() for s in soup.stripped_strings)

    summary = summarize_content(text)
    print("\n✅ Webpage Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()
