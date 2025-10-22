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


## creating .pynb file and setting kernel for the file :
Create openai_webscraper.ipynb file and set kernel by clicking on "Select kernel"(On the top right corner of the file), then in the Pop-up select "Python Environment" and then select ".venv"(i.e. the virtual environment "uv" created for you). It will set the kernel for you and now in place of "Select kernel" you will see ".venv(Python 3.12.13)" or something similar. It means kernel is set for the file.

