import pytest
from unittest.mock import Mock
from datetime import date, timedelta
from src.models import BookLoan
from src.fine_calculator import FineCalculator
from src.fine_notifier import FineNotifier
from src.library_service import LibraryService

class TestLibraryService:
    def setup_method(self):
        self.calc = FineCalculator()
        self.mock_notifier = Mock(spec=FineNotifier)
        self.service = LibraryService(self.calc, self.mock_notifier)

    def test_init_none_deps(self):
        with pytest.raises(ValueError):
            LibraryService(None, self.mock_notifier)
        with pytest.raises(ValueError):
            LibraryService(self.calc, None)

    def test_process_return_none_loan(self):
        with pytest.raises(ValueError, match="loan не может быть None"):
            self.service.process_return(None, "Reader")

    def test_process_return_empty_reader(self):
        loan = BookLoan(1, "Student", date.today(), date.today())
        with pytest.raises(ValueError, match="Имя читателя обязательно"):
            self.service.process_return(loan, "")
        with pytest.raises(ValueError, match="Имя читателя обязательно"):
            self.service.process_return(loan, "   ")

    def test_process_return_no_overdue(self):
        loan = BookLoan(1, "Student", date.today() - timedelta(days=5), date.today())
        fine = self.service.process_return(loan, "Test")
        assert fine == 0.0
        self.mock_notifier.notify_fine.assert_not_called()

    def test_process_return_overdue(self):
        loan = BookLoan(1, "Student", date.today() - timedelta(days=20), date.today())
        fine = self.service.process_return(loan, "StudentName")
        assert fine == 30.0
        self.mock_notifier.notify_fine.assert_called_once_with(30.0, "StudentName")

    def test_process_return_calculator_raises(self):
        loan = BookLoan(1, "Student", date.today(), None)  # не возвращена
        with pytest.raises(RuntimeError, match="Ошибка при обработке возврата"):
            self.service.process_return(loan, "Reader")
        self.mock_notifier.notify_fine.assert_not_called()
