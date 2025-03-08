from PySide6.QtWidgets import QToolBar, QDialog, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon

class PopupNotification(QDialog):
    def __init__(self, message, duration=3000, parent=None):
        super().__init__()
        self.setWindowTitle("Drink Water Reminder")
        self.setWindowIcon(QIcon("assets/icons/drop.png"))
        
        self.setFixedSize(300, 100)
        
        layout = QVBoxLayout(self)
        label = QLabel(message)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Automatically close the popup after the specified duration (in milliseconds)
        QTimer.singleShot(duration, self.close)

