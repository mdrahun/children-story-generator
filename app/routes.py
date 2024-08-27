from flask import Flask, request, jsonify, Response, send_file, send_from_directory

from app.image_generation import run_image
from app.story_generation import generate_story
from app.utils import generate_image_prompt, create_html_response, encode_image

app = Flask(__name__)

@app.route("/api/generate", methods=["POST"])
def generate_api():
    try:
        req_body = request.form
        if not req_body:
            raise ValueError("No form data received in request body.")

        theme = req_body.get("theme", "a general children's story")

        clean_text, full_text = generate_story(theme)
        image_prompt = generate_image_prompt(clean_text, theme)
        image_data = run_image(image_prompt, quality="high", style="digital art")
        encoded_image = encode_image(image_data)

        full_html = create_html_response(encoded_image, full_text, theme)

        return Response(full_html, content_type='text/html')
    except Exception as e:
        print(f'Error occurred: {str(e)}')
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return send_file('../web/index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../web', path)
