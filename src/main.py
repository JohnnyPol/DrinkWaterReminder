import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.tray_icon import TrayIcon
from core.reminder import Reminder

import os


def main():
    basedir = os.path.dirname(__file__)

    try:
        from ctypes import windll  # Only exists on Windows.
        myappid = 'mycompany.myproduct.subproduct.version'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
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

