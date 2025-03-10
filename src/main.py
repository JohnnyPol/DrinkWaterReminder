import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.tray_icon import TrayIcon
from core.reminder import Reminder

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    reminder = Reminder()
    
    main_window = MainWindow(reminder)

    tray = TrayIcon(reminder, main_window)
    tray.show()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

