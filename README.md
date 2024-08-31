# Kids Story Generator

Kids Story Generator is a web application that generates children's stories based on a user-provided theme. 
The application leverages modern AI tools to create engaging and creative stories for kids.

## Features

- Generate unique children's stories by entering a theme.
- Simple and intuitive web interface.
- Real-time story generation with related image

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mdrahun/children-story-generator.git
   cd children-story-generator
   ```

2. **Install dependencies using Poetry:**

   ```bash
   poetry install
   ```

3. **Activate the virtual environment:**

   ```bash
   poetry shell
   ```

## Usage

1. **Run the application:**

   ```bash
   poetry run python main.py
   ```

2. **Open your browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```

3. **Enter a theme for the story and click "Generate Story".**


### Production

1. **Run the application in production mode using Gunicorn:**

   ```bash
   poetry run gunicorn -w 4 -b 0.0.0.0:8000 main:app
   ```

2. **Open your browser and navigate to:**

   ```
   http://0.0.0.0:8000
   ```

## Dependencies

- Python 3.10+
- Flask 3.0.3
- LangChain
- Google Generative AI
- Requests
- Gunicorn
- python-dotenv


### Tech Stack

- Backend:
   - Python: Core programming language.
   - Flask: Web framework for routing and handling HTTP requests.
   - LangChain: Library for working with language models.
   - Google Generative AI: API for text generation.

- Frontend:
   - HTMX: Library for server-driven UI updates without JavaScript.
   - HTML/CSS: For structuring and styling web pages.

- Infrastructure:
   - Poetry: Dependency management and virtual environment setup.
   - Gunicorn: WSGI server.
