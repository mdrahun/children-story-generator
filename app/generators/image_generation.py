from typing import Optional

import requests

from app.config import Config
from app.exceptions import ImageGenerationError


def run_image(image_prompt: str, quality: str, style: str) -> Optional[bytes]:
    """Generate an image based on the provided prompt, quality, and style."""
    send_prompts = f"{image_prompt}, in {style} style, {quality} quality"

    headers = {"Authorization": f"Bearer {Config.HUGGINGFACE_API_TOKEN}"}

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/Artples/LAI-ImageGeneration-vSDXL-2",
            headers=headers,
            json={"inputs": send_prompts},
        )
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        # Log the error message or handle it as required
        raise ImageGenerationError(f"Image generation failed: {e}")
