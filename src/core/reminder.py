from PySide6.QtCore import QTimer, QObject, Signal
from .settings import settings

class Reminder(QObject):
    notify = Signal()  # Signal to trigger notification

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.trigger_notification)
        self.set_interval(settings["reminder_interval"])

    def set_interval(self, minutes):
        self.timer.stop()
        self.timer.start(minutes * 60 * 1000)  # Convert minutes to milliseconds

    def trigger_notification(self):
        if settings["enabled"]:
            self.notify.emit()  # Emit signal to notify user
