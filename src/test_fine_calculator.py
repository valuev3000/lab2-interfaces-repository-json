import pytest
from datetime import date, timedelta
from src.models import BookLoan
from src.fine_calculator import FineCalculator

class TestFineCalculator:
    def setup_method(self):
        self.calc = FineCalculator()

    def test_calculate_fine_none_loan(self):
        with pytest.raises(ValueError, match="loan не может быть None"):
            self.calc.calculate_fine(None)

    def test_calculate_fine_not_returned(self):
        loan = BookLoan(1, "Student", date.today(), None)
        with pytest.raises(ValueError, match="Книга ещё не возвращена"):
            self.calc.calculate_fine(loan)

    @pytest.mark.parametrize("category,loan_days_ago,due_days,overdue_days,rate,expected", [
        ("Student", 20, 14, 6, 5.0, 30.0),
        ("Teacher", 40, 30, 10, 2.0, 20.0),
        ("External", 10, 7, 3, 10.0, 30.0),
        ("Student", 10, 14, -4, 5.0, 0.0),
    ])
    def test_calculate_fine_various(self, category, loan_days_ago, due_days, overdue_days, rate, expected):
        loan_date = date.today() - timedelta(days=loan_days_ago)
        return_date = loan_date + timedelta(days=due_days + overdue_days)
        loan = BookLoan(1, category, loan_date, return_date)
        fine = self.calc.calculate_fine(loan)
        assert fine == expected

    @pytest.mark.parametrize("invalid_category", ["Unknown", ""])
    def test_calculate_fine_invalid_category(self, invalid_category):
        loan = BookLoan(1, invalid_category, date.today() - timedelta(days=10), date.today())
        with pytest.raises(ValueError, match="Неизвестная категория"):
            self.calc.calculate_fine(loan)
