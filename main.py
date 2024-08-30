from app import start_app
from app.config import Config

app = start_app()

if __name__ == '__main__':
    app.run(debug=Config.IS_DEBUG_ENABLED)