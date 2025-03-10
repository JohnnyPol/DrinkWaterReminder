from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon

class PopupNotification(QDialog):
    def __init__(self, message, duration=3000, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Drink Water Reminder")
        self.setWindowIcon(QIcon("assets/icons/drop.png"))
        # Frameless, tool window, and always on top so it doesn't steal focus
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(350, 100)
        
        # Apply custom stylesheet for a modern, polished look
        self.setStyleSheet("""
            QDialog {
                background-color: #3498db;
                border: 2px solid #2980b9;
                border-radius: 10px;
            }
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        label = QLabel(message)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        # Automatically close the popup after the specified duration (in milliseconds)
        QTimer.singleShot(duration, self.close)
