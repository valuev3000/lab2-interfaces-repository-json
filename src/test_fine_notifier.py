import pytest
from unittest.mock import Mock
from src.fine_notifier import FineNotifier

class TestFineNotifier:
    def test_init_none_service(self):
        with pytest.raises(ValueError, match="notification_service не может быть None"):
            FineNotifier(None)

    def test_notify_fine_empty_reader(self):
        mock_service = Mock()
        notifier = FineNotifier(mock_service)
        with pytest.raises(ValueError, match="Имя читателя не может быть пустым"):
            notifier.notify_fine(100.0, "")
        with pytest.raises(ValueError, match="Имя читателя не может быть пустым"):
            notifier.notify_fine(100.0, "   ")

    def test_notify_fine_calls_service(self):
        mock_service = Mock()
        notifier = FineNotifier(mock_service)
        notifier.notify_fine(75.5, "Иван Петров")
        mock_service.send_notification.assert_called_once()
        args, _ = mock_service.send_notification.call_args
        assert "75.5" in args[0]
        assert "Иван Петров" in args[0]
