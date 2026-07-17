import logging
import sys

logging.basicConfig(
    level=logging.CRITICAL,
    format="%(asctime)s [%(threadName)s] - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Writes to stdout
    ],
)

LOGGER = logging.getLogger(__name__)
