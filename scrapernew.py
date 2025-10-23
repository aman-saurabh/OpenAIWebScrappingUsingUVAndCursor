from playwright.sync_api import sync_playwright
import time
import os

def fetch_website_contents(url: str) -> str:
    """
    Uses Playwright to fetch fully-rendered HTML content,
    bypassing Cloudflare JS and cookie checks using saved session.
    """
    auth_file = "auth.json"
    if not os.path.exists(auth_file):
        raise FileNotFoundError(
            "❌ auth.json not found. Run collect_cookies.py first to generate it."
        )

    with sync_playwright() as p:
        # It is throwing erro if we use chromium instead of Firefox, so we are using p.firefox.launch inplace of p.chromium.launch

        browser = p.firefox.launch(headless=True)  # 👀 show browser temporarily
        context = browser.new_context(
            storage_state=auth_file,
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            locale="en-US",
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            permissions=["geolocation"]
        )

        page = context.new_page()
        print(f"🌐 Navigating to {url}...")

        try:
            page.goto(url, wait_until="networkidle", timeout=120000)
            time.sleep(10)  # allow JS to load fully

            # Detect if Cloudflare page appeared
            if "enable JavaScript" in page.content() or "Checking your browser" in page.content():
                raise Exception("⚠️ Cloudflare challenge detected. Try manual cookie refresh.")

            html = page.content()
            browser.close()
            return html

        except Exception as e:
            browser.close()
            print(f"❌ Error fetching website content: {e}")
            return None
