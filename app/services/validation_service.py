from flask import request

class ValidationService:
    """Service for validating request data."""

    @staticmethod
    def get_theme() -> str:
        """Extract the theme from the request form data."""
        req_body = request.form
        if not req_body:
            raise ValueError("No form data received in request body.")
        return req_body.get("theme", "a general children's story")