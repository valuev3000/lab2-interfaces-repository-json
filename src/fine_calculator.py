from datetime import date
from src.models import BookLoan

class FineCalculator:
    BASE_FINE_PER_DAY = 5.0
    TEACHER_FINE_PER_DAY = 2.0
    EXTERNAL_FINE_PER_DAY = 10.0

    def _get_due_days(self, category: str) -> int:
        mapping = {
            "Student": 14,
            "Teacher": 30,
            "External": 7,
        }
        if category not in mapping:
            raise ValueError(f"Неизвестная категория: {category}")
        return mapping[category]

    def _get_rate(self, category: str) -> float:
        mapping = {
            "Student": self.BASE_FINE_PER_DAY,
            "Teacher": self.TEACHER_FINE_PER_DAY,
            "External": self.EXTERNAL_FINE_PER_DAY,
        }
        if category not in mapping:
            raise ValueError(f"Неизвестная категория: {category}")
        return mapping[category]

    def calculate_fine(self, loan: BookLoan) -> float:
        if loan is None:
            raise ValueError("loan не может быть None")
        if loan.return_date is None:
            raise ValueError("Книга ещё не возвращена")

        due_date = loan.loan_date + timedelta(days=self._get_due_days(loan.reader_category))
        days_overdue = (loan.return_date - due_date).days
        if days_overdue <= 0:
            return 0.0
        rate = self._get_rate(loan.reader_category)
        return days_overdue * rate
