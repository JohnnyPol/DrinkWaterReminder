# 💧 Drink Water Reminder App

A simple and elegant reminder app designed to help you stay hydrated throughout your day! It periodically prompts you with customizable reminders to drink water.

---

## 🚀 Features
- 🔔 **Customizable Reminders:** Set reminders to drink water at custom intervals (hours, minutes, and seconds).
- 🌙 **Light/Dark Mode:** Switch between themes easily.
- 🔔 **Background Operation:** Minimizes to system tray and runs reminders in the background.
- 🎨 **Customizable UI:** A clean, modern interface with an attractive notification popup.

---

## 🛠️ Tech Stack
- **Python**
- **PySide6 (Qt Framework)** for GUI and Tray functionality.
- **PyInstaller** for packaging into an executable.

---

## 🚀 Getting Started

### 📌 Prerequisites
- **Python 3.8+** installed ([Download here](https://www.python.org/downloads/)).

### 🛠 Installation

1. Clone this repository or download the source code:
```bash
git clone <your_repo_link>
```

2. Navigate into the project directory and install dependencies:
```bash
pip install -r requirements.txt
```

### ▶ Running the Application

- Run the app from the project's root:
```bash
python -m src.main
```

The app will open a window to set the reminder interval and toggle themes.

---

## ⚙️ Packaging the Application (Windows)

To package your app as a Windows executable (`.exe`), use PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=assets/icons/drop.ico src/main.py
```

Your packaged app will appear in the `dist/` directory.

---

## 🚀 Running on Startup (Optional)

You can configure your app to run on startup by adding it to the Startup folder:

1. Press `Win + R`, type `shell:startup`, and press Enter.
2. Copy the `.exe` file from the `dist` folder and create a shortcut in the Startup folder.

---

## 📌 Using the App
- **Set interval:** Use the spin boxes to select how often reminders appear.
- Click **"Start"** to begin reminders and **"Stop"** to pause.
- Close (`X`) to minimize to system tray. Right-click the tray icon for options:
  - Show/hide the main window
  - Enable/disable reminders
  - Exit the application

---

## 🎨 Customizing the App
- Change icons or sounds by replacing files in the `assets/` folder.
- Adjust themes by editing the QSS stylesheets in `main_window.py`.

---

## 📝 Contributing
Feel free to fork, modify, or extend this app!

---

## 📜 License

This project is open-source, feel free to use, modify, and share!

