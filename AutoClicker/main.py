import pynput.mouse as mouse
import pynput.keyboard as keyboard
import threading
import time

clicking = False
enabled = False
click_speed = 0.001
cac = mouse.Controller()

print("MADE BY: geta1005")
print("TOGGLE KEY: F2")

def clicker():
    while True:
        if clicking and enabled:
            cac.click(mouse.Button.left, 1)
        time.sleep(click_speed)

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        global clicking
        clicking = not clicking

def on_press(key):
    if str(key) == "Key.f2":
        global enabled
        enabled = not enabled

def mouse_lis():
    with mouse.Listener(on_click=on_click) as listener1:
        listener1.join()

def keyboard_lis():
    with keyboard.Listener(on_press=on_press) as listener2:
        listener2.join()

thread_1 = threading.Thread(target=clicker)
thread_1.start()

thread_2 = threading.Thread(target=mouse_lis)
thread_2.start()

thread_3 = threading.Thread(target=keyboard_lis)
thread_3.start()
