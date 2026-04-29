from typing import Protocol

class NotificationService(Protocol):
    def send_notification(self, message: str) -> None:
        ...

class EmailNotificationService:
    def send_notification(self, message: str) -> None:
        # Реальная отправка email (заглушка для production)
        print(f"Email отправлен: {message}")
