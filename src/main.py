import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.tray_icon import TrayIcon
from core.reminder import Reminder
from core.notifier import show_notification

def main():
    app = QApplication(sys.argv)

    reminder = Reminder()
    reminder.notify.connect(show_notification)

    tray = TrayIcon(reminder)
    tray.show()

    window = MainWindow(reminder)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

