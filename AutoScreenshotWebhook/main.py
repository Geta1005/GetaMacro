import time
import pyautogui
import requests
from datetime import datetime, date

def gettime():
    return datetime.now().strftime("%H-%M-%S")
def getdate():
    return date.today().strftime("%Y-%m-%d")
def gettimedate():
    return str(getdate())+' '+str(gettime())

WEBHOOK_URL = input("WEBHOOK URL: ")
WAIT_TIME = int(input("WAIT TIME: "))
c = 0
if __name__ == "__main__":
    time.sleep(1)
    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save("autoscreenshot_webhook.png")
        response = requests.post(
            WEBHOOK_URL,
            data={"content": gettimedate()},
            files={"file": open("autoscreenshot_webhook.png", "rb")}
        )
        c = c + 1
        print("SENT #"+str(c))
        time.sleep(WAIT_TIME)
