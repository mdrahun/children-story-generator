import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class to store environment variables."""
    IS_DEBUG_ENABLED: bool = os.getenv("IS_DEBUG_ENABLED", "false").lower() == "true"
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    HUGGINGFACE_API_TOKEN: Optional[str] = os.getenv("HUGGINGFACE_API_TOKEN")

    @staticmethod
    def is_configured() -> bool:
        """Check if essential configuration variables are set."""
        return all([
            Config.GOOGLE_API_KEY,
            Config.HUGGINGFACE_API_TOKEN,
            Config.IS_DEBUG_ENABLED is not None
        ])
