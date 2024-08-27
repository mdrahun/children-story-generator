import requests
from app.config import Config

def run_image(image_prompt, quality, style):
    send_prompts = f"{image_prompt}, in {style} style, {quality} quality"

    headers = {"Authorization": f"Bearer {Config.HUGGINGFACE_API_TOKEN}"}
    response = requests.post(
        "https://api-inference.huggingface.co/models/Artples/LAI-ImageGeneration-vSDXL-2",
        headers=headers,
        json={"inputs": send_prompts},
    )

    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Image generation failed with status code {response.status_code}")