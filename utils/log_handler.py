import logging
from datetime import date
import os
import sys

from settings import BASE_DIR


def log(name, level=logging.INFO):
    try:
        if not os.path.exists('{}/logs/'.format(BASE_DIR)):
            os.mkdir('{}/logs/'.format(BASE_DIR))
        logger = logging.getLogger(name)
        logger.setLevel(level)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%b%y %H:%M:%S")

        file_handler = logging.FileHandler(f"{BASE_DIR}/logs/{date.today().strftime('%d-%m-%Y')}-app.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger
    except Exception as e:
        return {"code": 500, "message": str(e)}
