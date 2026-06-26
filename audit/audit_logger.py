import logging
from datetime import datetime

logging.basicConfig(
    filename='data/audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def log_event(event: str, agency: str = "system"):
    logging.info(f"[{agency}] {event}")