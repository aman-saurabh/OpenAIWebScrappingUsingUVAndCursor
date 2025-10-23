from playwright.sync_api import sync_playwright

def collect_cookies(url="https://openai.com"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 👀 shows browser window
        context = browser.new_context()
        page = context.new_page()
        print(f"Opening {url} in Chromium...")
        page.goto(url, wait_until="load", timeout=120000)
        input("✅ Once the page has loaded completely, press Enter here to save cookies...")
        context.storage_state(path="auth.json")
        browser.close()
        print("🎉 Cookies saved to auth.json")

if __name__ == "__main__":
    collect_cookies()
