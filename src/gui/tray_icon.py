from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction
import sys
import os

class TrayIcon(QSystemTrayIcon):
    def __init__(self, reminder, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon("assets/icons/drop.png"))
        self.reminder = reminder

        menu = QMenu(parent)
        
        toggle_action = QAction("Enable Reminders", self, checkable=True)
        toggle_action.setChecked(True)
        toggle_action.triggered.connect(self.toggle_reminders)
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(sys.exit)
        
        menu.addAction(toggle_action)
        menu.addSeparator()
        menu.addAction(exit_action)
        
        self.setContextMenu(menu)
        self.activated.connect(self.on_click)

    def toggle_reminders(self, checked):
        from core.settings import settings, save_settings
        settings["enabled"] = checked
        save_settings(settings)
    
    def on_click(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.showMessage("Drink Water Reminder", "Click here to open settings.")
