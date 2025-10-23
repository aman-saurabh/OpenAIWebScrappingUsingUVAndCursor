![OpenAI Web Scraping](https://img.shields.io/badge/OpenAI%20Web%20Scraping%20Using%20UV%20And%20Cursor%20%20%20|%20%20version-gray?style=flat)![v1.0.0](https://img.shields.io/badge/1.0.0-brightgreen?style=flat)

# OpenAI Web Scrapping Project Using UV and Cursor

## Initial setup commands
```
uv init
```
```
uv venv
```
```
.venv\Scripts\activate
```

## Install required packages for the project
```
uv add requests beautifulsoup4 openai python-dotenv pandas jupyter playwright
```
This command automatically updates your pyproject.toml and uv.lock file. But still if you want to add dependencies in requirement.txt file then run the following command.

### Command to list all packages in requirement.txt file
```
uv export --no-hashes --format requirements-txt > requirements.txt
```

## Install playwright
```
python -m playwright install
```
Command to check playwright version
```
python -m playwright --version
```

## Add OpenAI key in the ".env" file: 
Create a ".env" file in the project directory and add the OpenAI key in the file as follows.
```
OPENAI_API_KEY=your_openai_api_key_here
```

You can get your OpenAI API key from the following URL: 
* https://platform.openai.com/settings/organization/api-keys


## creating .ipynb file and setting kernel for the file :
Create openai_webscraper.ipynb file and set kernel by clicking on "Select kernel"(On the top right corner of the file), then in the Pop-up select "Python Environment" and then select ".venv"(i.e. the virtual environment "uv" created for you). It will set the kernel for you and now in place of "Select kernel" you will see ".venv(Python 3.12.13)" or something similar. It means kernel is set for the file.

## How to add code in a cell in ".ipynb" file :
In the ".ipynb" file click on the "+ Code" button to add a cell 

## How to run a cell :
When you hover over a cell it shows a "horizontal triangle" symbol. If you hover over that triangle it shows the text "Execute cell". Click on this triangle to run the cell.

## How to run all cells i.e. complete file programs :
On the Top you will see a "Horizoontal double triangle" symbol folled by "Run all". Cick on this button to run complete program.

We can also run complete program from the terminal using following command :
```
jupyter nbconvert --to notebook --execute openai_webscraper.ipynb --inplace
```

# How to run openai_playwright_webscrapping.py file :
For web scrapping of client side rendering/dynamic rendering websites we need headless browser and JS Engine.
So let's understand few associated terms first. 
## Server-Side Rendering (SSR) -> 
* The server generates the full HTML page before sending it to the browser. The browser just renders the HTML.
* Example - Classic sites, blogs, most news sites
* Scraping Approach - Simple requests.get(url) works. You get the full HTML directly.

## Client-Side Rendering (CSR) -> 
* The server sends minimal HTML + JavaScript. The browser runs JS to fetch data and build the DOM dynamically.
* Example - React, Vue, Angular apps (like https://openai.com)
* Scraping Approach - Must use a headless browser / JS engine (Playwright, Selenium) to render the page before scraping.

## Hybrid / Dynamic Rendering -> 
* Some content is SSR, some CSR. Example: initial HTML is rendered by server, then JS fills dynamic parts.
* Example - Medium, e-commerce product pages
* Scraping Approach - Sometimes requests.get() works for basic info, but dynamic parts require Playwright/Selenium.

## Browser automation ->
Browser automation means programmatically controlling a web browser — simulating user actions like:

* Opening pages

* Clicking buttons

* Filling out forms

* Extracting data (web scraping)

* Testing web applications

### Examples:
* Selenium (Python, Java, JS)

* Puppeteer (Node.js)

* Playwright (multi-language)

* Cypress (testing)

### Concept:
You write code that interacts with a browser driver or API to perform tasks automatically instead of manually.

## Headless Browsing ->
A headless browser is a browser without a graphical user interface (GUI).
It behaves like Chrome or Firefox but runs in the background — you can’t see the window.

### Purpose:
* Faster and lighter (no rendering to screen)

* Ideal for automation and web scraping

* Common in continuous integration (CI/CD) testing

### Examples:
* Headless Chrome

* Headless Firefox

* Playwright headless mode

## JavaScript Engine ->
A JavaScript Engine is the core program inside the browser that executes JavaScript code.
Every modern browser has one.

### Examples:
* Google Chrome, Microsoft Edge, NodeJS ---> V8
* Firefox ---> SpiderMonkey
* Safari ---> JavaScriptCore(Nitro)

So, https://openai.com is a client side rendering website and we need some headless browser to read it's content. Here we are using PlayWright for headless browsing. Apart from that the website has some Cloudflare JS and cookie checks, so to bypass that we are first running collect_cookies.py file which collects cookies and save them in "auth.json" file and we use this auth.json file in browser.new_context() in scrapernew.py file to pass cookies to bypass Cloudflare JS and cookie checks.

So, to run "openai_playwright_webscrapping.py" program first run "collect_cookies.py" file using command :
```
python collect_cookies.py
```
It will open a browser window. Wait for 5-7 seconds and then press "Enter" to close the browser window. It will save the cookies in "auth.json" file.

Now run "openai_playwright_webscrapping.py" command using the following command :
```
python openai_playwright_webscrapping.py
```
It will show you the website summary.

# Explanation of Playwright code used in the project : 
```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://openai.com")
    print(page.title())
```
## with sync_playwright() as p: — Full Explanation
### The Concept: Context Manager (with ... as ...)
In Python, the "with" keyword is used to create a context manager — an object that sets something up before the block of code runs and automatically cleans it up afterward.

For example :
```
with open("data.txt") as file:
    content = file.read()
```
* open("data.txt") → opens the file "data/txt" and saves it in a variable "file".

* file → variable that represents the open file object

* When the block ends → Python automatically closes the file, even if an error occurs.

So the same pattern is used by Playwright to safely start and stop its browser automation service in the above code.

# Explanation of full code block:
```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://openai.com")
    print(page.title())
```

* sync_playwright() -> Starts the Playwright engine(i.e. browser automation service) in synchronous mode (so you can use normal Python code, async/await is not required).
* as p: -> Assigns the Playwright controller object to the variable p.
* browser = p.chromium.launch() -> Launches a Chromium browser instance that Playwright controls. You could also use "p.firefox" or "p.webkit". This browser instance is saved into "browser" variable.
* headless=True -> headless=True means perform headless browsing i.e. don't open the Graphical User Iterface of the browser i.e. perform the browsing in background while headless=False means open the browser in GUI.
* page = browser.new_page() -> Opens a new browser tab and saves into "page" variable.
* page.goto("https://openai.com") -> Opens the given URL(i.e. "https://openai.com") in the new tab(which was saved in "page" variable).
* (after block ends) -> Automatically closes all browsers and background processes.

So, it is the simplifies version for equivalent code :
```
from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch()
page = browser.new_page()
page.goto("https://openai.com")
p.stop()  # You must remember to stop manually
```

## Difference between sync_playwright() and async_playwright() of Playwright :
### Sync Playwright (sync_playwright())
* Provides blocking / synchronous API.

* Code executes line by line. 

* Works fine in a normal Python script.

* Example :
```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://openai.com")
    print(page.title())
    browser.close()
```

### Async Playwright (async_playwright())
* Provides async / non-blocking API using await.

* Must be run inside an asyncio loop.

* This allows multiple pages or browsers to be launched concurrently.

* Example:
```
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://openai.com")
        print(await page.title())
        await browser.close()

asyncio.run(main())
```

## 👤 Author

**Aman Saurabh**  
💼 GitHub: [@aman-saurabh](https://github.com/aman-saurabh)  
