import base64

def generate_image_prompt(clean_text, theme):
    image_prompt = f"""
    I'm generating a story about {theme}.
    Here is the story: "{clean_text}".
    I need an image to accompany this story.
    Generate an image prompt that would help create an image related to this story.
    """
    return image_prompt

def create_html_response(encoded_image, full_text, theme):
    full_html = f"""
    <br/>
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image}" alt="Image related to {theme}" style="width:500px; height:auto;" />
    </div>
    <div style="text-align: left;">
        <blockquote>{full_text}</blockquote>
    </div>
    """
    return full_html

def encode_image(image_data):
    return base64.b64encode(image_data).decode('utf-8')