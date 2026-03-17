from dataclasses import dataclass
from datetime import datetime


@dataclass
class URL:
    original_url: str
    short_code: str
    created_at: datetime

