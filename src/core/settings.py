import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "../../config.json")

DEFAULT_CONFIG = {
    "reminder_interval": 10,  # in minutes
    "enabled": True
}

def load_settings():
    if not os.path.exists(CONFIG_FILE):
        save_settings(DEFAULT_CONFIG)
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def save_settings(settings):
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings, file, indent=4)

settings = load_settings()  # Load settings on startup
