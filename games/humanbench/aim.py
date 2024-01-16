import time
import pyautogui
from PIL import ImageGrab
import keyboard 

top_left = (404, 238)
bottom_right = (1365, 717)
pyautogui.PAUSE = 0

def aim():
    screen = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    width, height = screen.size
    for x in range(width):
        for y in range(height):
            r, g, b, _ = screen.getpixel((x, y))
            xr, xg, xb = 163, 195, 229
            if r == xr and g == xg and b == xb:
                pyautogui.moveTo(x + top_left[0], y + top_left[1])
                pyautogui.click()
                return 

while True:
    if keyboard.is_pressed('q'):
        break
    aim()
