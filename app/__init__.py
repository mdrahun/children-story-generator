from flask import Flask

from app.routes import app


def start_app() -> Flask:
    """Initialize and return the Flask application instance."""
    return app
