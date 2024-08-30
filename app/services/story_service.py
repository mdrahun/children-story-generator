from typing import Tuple

from app.generators import run_image, generate_text_story
from app.utils import generate_image_prompt, create_html_response, encode_image


class StoryService:
    """Service for generating stories and images."""

    @staticmethod
    def generate_story_content(theme: str) -> Tuple[str, str]:
        """Generate the story content based on the theme."""
        clean_text, full_text = generate_text_story(theme)
        return clean_text, full_text

    @staticmethod
    def generate_image_for_story(clean_text: str, theme: str) -> bytes:
        """Generate the image based on the clean text and theme."""
        image_prompt = generate_image_prompt(clean_text, theme)
        return run_image(image_prompt, quality="high", style="digital art")

    @staticmethod
    def create_full_response(encoded_image: str, full_text: str, theme: str) -> str:
        """Create the full HTML response with the image and text."""
        return create_html_response(encoded_image, full_text, theme)

    @staticmethod
    def encode_image_data(image_data: bytes) -> str:
        """Encode image data to a string format."""
        return encode_image(image_data)
