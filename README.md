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
uv add requests beautifulsoup4 openai python-dotenv pandas jupyter
```
This command automatically updates your pyproject.toml and uv.lock file. But still if you want to add dependencies in requirement.txt file then run the following command.

### Command to list all packages in requirement.txt file
```
uv export --no-hashes --format requirements-txt > requirements.txt
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

## 👤 Author

**Aman Saurabh**  
💼 GitHub: [@aman-saurabh](https://github.com/aman-saurabh)  
