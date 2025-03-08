from plyer import notification

def show_notification():
    notification.notify(
        title="Drink Water Reminder",
        message="Time to drink some water! Stay hydrated 💧",
        app_name="Drink Water App"
    )
