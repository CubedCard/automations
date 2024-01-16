import pyautogui
import time
from PIL import ImageGrab
import keyboard 
from pynput import mouse

top_left = (759, 294)
bottom_right = (1151, 684)
pyautogui.PAUSE = 0

blocks = [
        (820, 359), (951, 359), (1083, 359),
        (820, 491), (951, 491), (1083, 491),
        (820, 619), (951, 619), (1083, 619)
        ]

click_count = 0

def clickAllPos(cords):
    for pos in cords[-get_total_clicks()-1:]:
        pyautogui.moveTo(pos)
        pyautogui.click()
        time.sleep(0.01)

def findColor(r,g,b):
    image = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    for x, y in blocks:
        x, y = x - top_left[0], y - top_left[1]
        px = image.getpixel((x, y))
        if px[0] == r and px[1] == g and px[2] == b:
            return (x + top_left[0],y + top_left[1])

cords = []

def get_total_clicks():
    c = int(click_count)
    for t in range(click_count):
        c -= t
        if c == 0:
            return t
    return -1

def on_click(x, y, button, pressed):
    global click_count

    if button == mouse.Button.left and pressed:
        click_count += 1

listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    if keyboard.is_pressed('q'):
        break
    if keyboard.is_pressed('c'):
        clickAllPos(cords)
    pos = findColor(255, 255, 255)
    if pos: 
        if pos not in cords or pos != cords[-1]:
            cords.append(pos)
            pyautogui.moveTo(pos)

