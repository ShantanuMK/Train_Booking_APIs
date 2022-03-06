import os
from pathlib import Path


BASE_DIR: str = os.path.abspath(Path(__file__).parent)
DEBUG_LEVEL: bool = True
COACHES = {
    "A/C Sleeper" : {"max_seats": 60},
    "NON A/C Sleeper" : {"max_seats": 60},
    "SEATER": {"max_seats": 120}
}
