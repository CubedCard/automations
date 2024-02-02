import cv2
from PIL import ImageGrab
import pytesseract
import pyautogui
import numpy as np

top_left = (410, 400)
bottom_right = (1371, 507)
pyautogui.PAUSE = 0

while True:
    screenshot = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = pytesseract.image_to_string(img_gray, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789 --dpi 70')

    if result.strip().isdigit():
        print(result.strip())
        r, g, b = 56, 109, 182
        while ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1])).getpixel((100, 50)) != (r, g, b, 255):
            continue
        for char in result.strip():
            pyautogui.press(char)
        pyautogui.press('enter')
        pyautogui.press('enter')

