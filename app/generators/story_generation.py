from typing import Tuple

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


def generate_text_story(theme: str) -> Tuple[str, str]:
    """Generate a children's story based on the given theme."""
    try:
        model = ChatGoogleGenerativeAI(model="gemini-pro")
        prompt = f"Generate a children's story about {theme}."
        message = HumanMessage(content=prompt)
        response = model.stream([message])

        full_text = ""
        for chunk in response:
            full_text += chunk.content

        clean_text = f"<div><p>{' '.join(full_text.split())}</p></div>"
        return clean_text, full_text

    except Exception as e:
        # Add appropriate logging or error handling here
        raise RuntimeError(f"Failed to generate text story: {str(e)}")
