import logging
import os

logging.getLogger("httpx").setLevel(logging.WARNING)

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("logs/bot.log")
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logger()