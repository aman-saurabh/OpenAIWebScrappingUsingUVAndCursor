# scraper.py
import requests

def fetch_website_contents(url: str) -> str:
    """
    Fetch the raw HTML content of a website.

    Args:
        url (str): The website URL.

    Returns:
        str: Raw HTML content of the page, or empty string on error.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website content: {e}")
        return ""
