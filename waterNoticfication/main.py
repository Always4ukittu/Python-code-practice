
import time
from plyer import notification

while True:
    if __name__ == "__main__":
        notification.notify(
            title = "Please Drink Water",
            message = " Drinking water helps make you alive. And beneficial for your health.\
                        Aleast a normal human must drink 8 ltrs of water a day. This makes person hydrated. ",
            app_icon = "glass.ico",
            timeout = 5  # notification will disappears after
        )
        time.sleep(60*50) # after flashing notification it sleep for 3600 seconds then flash
        # to run in background run "pythonw.exe ./main.py" in terminal 
