from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction
from core.settings import settings
import sys

class TrayIcon(QSystemTrayIcon):
    def __init__(self, reminder, main_window, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon("assets/icons/drop.png"))
        self.reminder = reminder
        self.main_window = main_window

        menu = QMenu(parent)
        
        show_action = QAction("Show Window", self)
        show_action.triggered.connect(self.show_main_window)

        toggle_action = QAction("Enable Reminders", self, checkable=True)
        checked = settings["enabled"]
        toggle_action.setChecked(checked)
        toggle_action.triggered.connect(self.toggle_reminders)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)

        menu.addAction(show_action)
        menu.addAction(toggle_action)
        menu.addSeparator()
        menu.addAction(exit_action)

        self.setContextMenu(menu)
        self.activated.connect(self.on_click)

    def show_main_window(self):
        """Show the main window if it's hidden."""
        self.main_window.showNormal()
        self.main_window.activateWindow()
    
    def toggle_reminders(self, checked):
        from core.settings import save_settings
        settings["enabled"] = checked
        save_settings(settings)
        if checked:
            # Start the timer again
            self.reminder.set_interval(settings["reminder_interval"])
        else:
            self.reminder.timer.stop()

    
    def on_click(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show_main_window()
    
    def exit_app(self):
        """Properly quit the application."""
        sys.exit()