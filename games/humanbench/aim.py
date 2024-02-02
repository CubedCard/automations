import pyautogui
from PIL import ImageGrab
import numpy as np
import time

top_left = (473, 247)
bottom_right = (1365, 717)
start_button = (888, 462)
pyautogui.PAUSE = 0

def aim():
    clicks_left = 30
    while clicks_left > 0:
        screenshot = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
        screenshot_array = np.array(screenshot)

        target_color = (163, 195, 229, 255)

        if np.any(np.all(screenshot_array == np.array(target_color), axis=-1)):
            target_position = np.argwhere(np.all(screenshot_array == np.array(target_color), axis=-1))[0]
            x, y = target_position[1], target_position[0]
            pyautogui.click(x + top_left[0], y + top_left[1])
            clicks_left -= 1
        else:
            print("Target color not found in the screenshot.")
            break

if __name__ == "__main__":
    time.sleep(1)
    pyautogui.moveTo(start_button[0], start_button[1])
    pyautogui.click()
    aim()
