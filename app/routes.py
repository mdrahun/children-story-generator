from flask import Flask, jsonify, Response, send_file, send_from_directory, make_response

from app.exceptions import ImageGenerationError
from app.services.story_service import StoryService
from app.services.validation_service import ValidationService

app = Flask(__name__)


def generate_story() -> Response:
    """Generate the complete story with an image and return the HTML response."""
    theme = ValidationService.get_theme()
    clean_text, full_text = StoryService.generate_story_content(theme)

    try:
        image_data = StoryService.generate_image_for_story(clean_text, theme)
    except ImageGenerationError as e:
        app.logger.error(f"Image generation failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to generate image."}), 500)

    encoded_image = StoryService.encode_image_data(image_data)
    full_html = StoryService.create_full_response(encoded_image, full_text, theme)
    return Response(full_html, content_type='text/html')


@app.route("/api/generate", methods=["POST"])
def generate_api() -> Response:
    try:
        return generate_story()
    except ValueError as e:
        app.logger.error(f'Validation error: {str(e)}')
        return make_response(jsonify({"error": str(e)}), 400)
    except Exception as e:
        app.logger.error(f'Unexpected error occurred: {str(e)}')
        return make_response(jsonify({"error": "An unexpected error occurred."}), 500)


@app.route('/')
def home() -> Response:
    return send_file('../web/index.html')


@app.route('/<path:path>')
def serve_static(path: str) -> Response:
    return send_from_directory('../web', path)
