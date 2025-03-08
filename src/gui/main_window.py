from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout, 
    QMainWindow, 
    QVBoxLayout, 
    QLabel, 
    QSpinBox, 
    QPushButton
)
from PySide6.QtGui import QIcon, QCloseEvent, Qt
from core.settings import settings, save_settings
from core.notifier import PopupNotification
from PySide6.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self, reminder):
        super().__init__()
        self.reminder = reminder
        self.reminder.notify.connect(self.custom_show_notification)
        
        self.setWindowTitle("Drink Water Reminder")
        self.resize(800, 600)

        # Set window icon here:
        self.setWindowIcon(QIcon("assets/icons/drop.png"))
        
         # Create a central widget and set the layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # --- Timer Editor Section ---
        timer_label = QLabel("Set reminder interval (minutes):")
        self.interval_box = QSpinBox()
        self.interval_box.setRange(1, 120)
        self.interval_box.setValue(settings["reminder_interval"])

        main_layout.addWidget(timer_label)
        main_layout.addWidget(self.interval_box)

        # --- Buttons Section ---
        button_layout = QHBoxLayout()

        # Start button: saves the new interval and starts the reminder timer
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_reminders)
        button_layout.addWidget(self.start_button)

        # Stop button: stops the reminder timer
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_reminders)
        button_layout.addWidget(self.stop_button)

        main_layout.addLayout(button_layout)

        # Set the central widget of the QMainWindow
        self.setCentralWidget(central_widget)

    def start_reminders(self):
        # Update settings with the new interval from the spin box
        settings["reminder_interval"] = self.interval_box.value()
        save_settings(settings)
        # (Re)start the reminder timer with the updated interval
        self.reminder.set_interval(settings["reminder_interval"])
        # In case the timer was stopped, ensure it is active
        if not self.reminder.timer.isActive():
            self.reminder.timer.start(settings["reminder_interval"] * 60 * 1000)

    def stop_reminders(self):
        # Stop the reminder timer
        self.reminder.timer.stop()

    def save_settings_button(self):
        settings["reminder_interval"] = self.interval_box.value()
        save_settings(settings)
        self.reminder.set_interval(settings["reminder_interval"])
    
    def custom_show_notification(self):
        popup = PopupNotification("Time to drink water! Stay hydrated 💧")
        popup.setAttribute(Qt.WA_DeleteOnClose)
        popup.exec()
        
    
    def closeEvent(self, event: QCloseEvent):
        """
        Override the close event to hide the window instead of quitting.
        This keeps the app running in the background.
        """
        self.hide()
        # Show a balloon tip or tray message if desired:
        # e.g., self.tray_icon.showMessage("Drink Water Reminder", "Minimized to tray!")
        event.ignore()  # Prevent the window from actually closing.

