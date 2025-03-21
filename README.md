# 💧 Drink Water Reminder App
![OS](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Python](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10%20|%203.11-blue.svg?style=for-the-badge)
![Version 1.0.0](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://choosealicense.com/licenses/mit/)


	
> A simple and elegant reminder app designed to help you stay hydrated throughout your day! It periodically prompts you with customizable reminders to drink water.

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

### 🛠 Installation via Installer

For end-users, the easiest way to install the Drink Water Reminder app is via the installer from the repository's [release](https://github.com/JohnnyPol/DrinkWaterReminder/releases/tag/v1.0.0). <br> Once you run the installer:
1. You will find the application under C:\Program Files (x86)\DrinkWaterReminder\

2. A shortcut may be created on your **desktop** or in your **Start menu** (depending on your installer settings).

3. Simply run `DrinkWaterReminder.exe` to launch the application.

With the installer, you do **not** need Python installed.


### 🛠 Installation via Source

1. Clone this repository or download the source code:
```bash
git clone https://github.com/JohnnyPol/DrinkWaterReminder.git
```

2. Navigate into the project directory and install dependencies:
```bash
cd DrinkWaterReminder
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
pyinstaller --onefile --noconsole --icon=assets/icons/favicon.ico --add-data="assets;assets" src/main.py
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
- Close (`X`) to minimize to the system tray. Right-click the tray icon for options:
  - Show/hide the main window
  - Enable/disable reminders
  - Exit the application

---

## 🎨 Customizing the App
- Change icons or sounds by replacing files in the `assets/` folder.
- Adjust themes by editing the QSS stylesheets in `main_window.py`.

---

## 📝 Contributing
Feel free to fork, modify, or extend this app! <br>
Any contribution is more than welcome!

---

