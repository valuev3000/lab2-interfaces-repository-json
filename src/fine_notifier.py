from src.notification import NotificationService

class FineNotifier:
    def __init__(self, notification_service: NotificationService):
        if notification_service is None:
            raise ValueError("notification_service не может быть None")
        self._notification_service = notification_service

    def notify_fine(self, amount: float, reader_name: str) -> None:
        if not reader_name or not reader_name.strip():
            raise ValueError("Имя читателя не может быть пустым")
        message = f"Уважаемый {reader_name}, на вас наложен штраф в размере {amount} руб. за просрочку возврата книги."
        self._notification_service.send_notification(message)
