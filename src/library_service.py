from src.models import BookLoan
from src.fine_calculator import FineCalculator
from src.fine_notifier import FineNotifier

class LibraryService:
    def __init__(self, calculator: FineCalculator, notifier: FineNotifier):
        if calculator is None:
            raise ValueError("calculator не может быть None")
        if notifier is None:
            raise ValueError("notifier не может быть None")
        self._calculator = calculator
        self._notifier = notifier

    def process_return(self, loan: BookLoan, reader_name: str) -> float:
        if loan is None:
            raise ValueError("loan не может быть None")
        if not reader_name or not reader_name.strip():
            raise ValueError("Имя читателя обязательно")

        try:
            fine = self._calculator.calculate_fine(loan)
            if fine > 0:
                self._notifier.notify_fine(fine, reader_name)
            return fine
        except Exception as e:
            # Оборачиваем исключение для сохранения контекста
            raise RuntimeError("Ошибка при обработке возврата") from e
