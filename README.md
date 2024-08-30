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

## Notes

- In a production environment, it is recommended to use Gunicorn or another WSGI server instead of the built-in Flask development server.
- Ensure that all required environment variables are set up correctly for the application to function.
