from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class BookLoan:
    id: int
    reader_category: str   # "Student", "Teacher", "External"
    loan_date: date
    return_date: Optional[date] = None

    def __post_init__(self):
        if not self.reader_category:
            raise ValueError("reader_category не может быть пустым")
