from PySide6.QtWidgets import QToolBar, QMainWindow, QVBoxLayout, QLabel, QSpinBox, QPushButton
from PySide6.QtGui import QIcon
from core.settings import settings, save_settings

class MainWindow(QMainWindow):
    def __init__(self, reminder):
        super().__init__()
        self.reminder = reminder
        
        self.setWindowTitle("Drink Water Reminder")
        self.resize(1000, 800)

        # Set window icon here:
        self.setWindowIcon(QIcon("assets/icons/drop.png"))
        
        layout = QVBoxLayout()
        print(settings)
        self.label = QLabel("Set reminder interval (minutes):")
        self.interval_box = QSpinBox()
        self.interval_box.setRange(1, 120)
        self.interval_box.setValue(settings["reminder_interval"])
        
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_settings_button)

        layout.addWidget(self.label)
        layout.addWidget(self.interval_box)
        layout.addWidget(self.save_button)
        
        self.setLayout(layout)

    def save_settings_button(self):
        settings["reminder_interval"] = self.interval_box.value()
        save_settings(settings)
        self.reminder.set_interval(settings["reminder_interval"])
