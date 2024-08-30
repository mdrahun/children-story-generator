import base64


def generate_image_prompt(clean_text: str, theme: str) -> str:
    """Generate a prompt for image generation based on the story content and theme."""
    image_prompt = f"""
    I'm generating a story about {theme}.
    Here is the story: "{clean_text}".
    I need an image to accompany this story.
    Generate an image prompt that would help create an image related to this story.
    """
    return image_prompt.strip()


def create_html_response(encoded_image: str, full_text: str, theme: str) -> str:
    """Create an HTML response containing the encoded image and the full text of the story."""
    full_html = f"""
    <br/>
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image}" alt="Image related to {theme}" style="width:500px; height:auto;" />
    </div>
    <div style="text-align: left;">
        <blockquote>{full_text}</blockquote>
    </div>
    """
    return full_html.strip()


def encode_image(image_data: bytes) -> str:
    """Encode image data to a base64 string."""
    return base64.b64encode(image_data).decode('utf-8')
