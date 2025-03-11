from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout, 
    QMainWindow, 
    QVBoxLayout, 
    QLabel, 
    QSpinBox, 
    QPushButton,
    QToolButton
)
from PySide6.QtGui import QIcon, QCloseEvent, Qt, QFont, QFontDatabase
from core.settings import settings, save_settings
from core.notifier import PopupNotification


class MainWindow(QMainWindow):
    def __init__(self, reminder):
        super().__init__()
        self.reminder = reminder
        self.reminder.notify.connect(self.custom_show_notification)
        
        self.setWindowTitle("Drink Water Reminder")
        self.resize(800, 600)
        self.setWindowIcon(QIcon("assets\icons\drop.png"))
        
        # Define styles for light and dark themes
        self.light_theme = """
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel#HeaderLabel {
                font-size: 40px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
            }
            QLabel {
                font-size: 30px;
                color: #555555;
            }
            QSpinBox {
                font-size: 16px;
                padding: 5px;
                border: 1px solid #cccccc;
                border-radius: 4px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c5980;
            }
        """

        self.dark_theme = """
            QMainWindow {
                background-color: #2c3e50;
            }
            QLabel#HeaderLabel {
                font-size: 40px;
                font-weight: bold;
                color: #ecf0f1;
                padding: 10px;
            }
            QLabel {
                font-size: 30px;
                color: #bdc3c7;
            }
            QSpinBox {
                font-size: 16px;
                padding: 5px;
                border: 1px solid #34495e;
                border-radius: 4px;
                background-color: #34495e;
                color: white;
            }
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #922b21;
            }
        """
        
        self.current_theme = 'light'
        self.setStyleSheet(self.light_theme)
        
        # Create a central widget and set the layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Header Section
        header_layout = QHBoxLayout()
        header_label = QLabel("Drink Water Reminder")
        header_label.setObjectName("HeaderLabel")
        header_label.setAlignment(Qt.AlignCenter)
        # Load the custom font from the TTF file
        font_id = QFontDatabase.addApplicationFont("assets/fonts/Cookie-Regular.ttf")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            custom_font = QFont(font_family)  
            header_label.setFont(custom_font)
            header_label.font().setPointSize(50)
        else:
            print("Failed to load custom font.")
        
        main_layout.addWidget(header_label)
        main_layout.addLayout(header_layout)
        main_layout.addWidget(header_label)
        
        # --- Timer Editor Section ---
        timer_layout = QVBoxLayout()
        timer_label = QLabel("Set reminder interval:")
        timer_label.setFont(QFont("Cookie", 24))
        timer_layout.addWidget(timer_label)
        

        time_input_layout = QHBoxLayout()
        
        self.hours_box = QSpinBox()
        self.hours_box.setRange(0, 23)
        self.hours_box.setSuffix(" h")
        self.hours_box.setValue(settings.get("reminder_hours", 0))
        time_input_layout.addWidget(self.hours_box)
        
        self.minutes_box = QSpinBox()
        self.minutes_box.setRange(0, 59)
        self.minutes_box.setSuffix(" m")
        self.minutes_box.setValue(settings.get("reminder_minutes", settings["reminder_interval"]))
        time_input_layout.addWidget(self.minutes_box)
        
        self.seconds_box = QSpinBox()
        self.seconds_box.setRange(0, 59)
        self.seconds_box.setSuffix(" s")
        self.seconds_box.setValue(settings.get("reminder_seconds", 0))
        time_input_layout.addWidget(self.seconds_box)
        timer_layout.addLayout(time_input_layout)
        main_layout.addLayout(timer_layout)
        
        # --- Buttons Section ---
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        
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

        # Create a toggle switch in the top right corner
        self.theme_toggle_button = QToolButton()
        self.theme_toggle_button.setCheckable(True)
        # False means light mode (default) and True means dark mode
        self.theme_toggle_button.setChecked(False)
        # Set initial icon to sun (light mode)
        self.sun_icon = QIcon("assets/icons/sun.png")
        self.moon_icon = QIcon("assets/icons/moon.png")
        self.theme_toggle_button.setIcon(self.sun_icon)
        self.theme_toggle_button.clicked.connect(self.toggle_theme)
        self.theme_toggle_button.setStyleSheet("""
            QToolButton {
            background-color: #ecf0f1;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            padding: 5px;
            }
            QToolButton:checked {
            background-color: #34495e;
            color: white;
            }
        """)
        # Place the toggle switch as a corner widget in the top right
        # Create a layout for the top bar
        top_bar_layout = QHBoxLayout()
        top_bar_layout.addStretch()
        top_bar_layout.addWidget(self.theme_toggle_button)
        
        # Add the top bar layout to the main layout
        main_layout.insertLayout(0, top_bar_layout)

    def start_reminders(self):
         # Retrieve hours, minutes, and seconds from the UI spin boxes
        hours = self.hours_box.value()
        minutes = self.minutes_box.value()
        seconds = self.seconds_box.value()
        
        # Compute total seconds
        total_seconds = hours * 3600 + minutes * 60 + seconds
        if total_seconds <= 0:
            # Ensure there's at least a minimum interval (e.g., 60 seconds)
            total_seconds = 60

        # Update settings with the new interval values
        settings["reminder_hours"] = hours
        settings["reminder_minutes"] = minutes
        settings["reminder_seconds"] = seconds
        # Store the total interval in minutes (as a float) for backward compatibility with Reminder.set_interval
        settings["reminder_interval"] = total_seconds / 60.0
        save_settings(settings)
        
        # (Re)start the reminder timer using the computed interval
        self.reminder.set_interval(settings["reminder_interval"])


    def stop_reminders(self):
        # Stop the reminder timer
        self.reminder.timer.stop()

    def custom_show_notification(self):
        popup = PopupNotification("Time to drink water! Stay hydrated 💧", parent=self)
        popup.setAttribute(Qt.WA_DeleteOnClose)
        # Store the popup reference to prevent garbage collection
        self.notification_popup = popup
        popup.destroyed.connect(lambda: setattr(self, "notification_popup", None))
        popup.show()
    
    def toggle_theme(self):
        if self.theme_toggle_button.isChecked():
            self.current_theme = 'dark'
            self.setStyleSheet(self.dark_theme)
            self.theme_toggle_button.setIcon(self.moon_icon)
        else:
            self.current_theme = 'light'
            self.setStyleSheet(self.light_theme)
            self.theme_toggle_button.setIcon(self.sun_icon)
    
    def closeEvent(self, event: QCloseEvent):
        """
        Override the close event to hide the window instead of quitting.
        This keeps the app running in the background.
        """
        self.hide()
        event.ignore()  # Prevent the window from actually closing.
