from PIL import ImageGrab
import pytesseract
import pyautogui
import cv2
import numpy as np
import time

top_left = (989, 371)
bottom_right = (1682, 965)

words = []
with open('/usr/share/dict/words', 'r') as file:
    words = file.read().splitlines()

start_pos = (1329, 685)

pyautogui.PAUSE = 0
custom_oem_psm_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ"'

def get_text():
    screenshot = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    screenshot.save('test.png')
    letters = pytesseract.image_to_string(img_gray, lang='eng', config=custom_oem_psm_config).strip()
    return ''.join(filter(str.isalpha, letters))

def get_posibilities(chars):
    posibilities = []
    for word in words:
        used_chars = []
        if len(word) > len(chars) or len(word) < 4:
            continue
        for char in word:
            if char.lower() not in chars.lower() or char.lower() in used_chars:
                break
            if char.lower() in chars.lower():
                used_chars.append(char.lower())
        else:
            posibilities.append(word)
    return [x for x in posibilities if 'a' in x.lower()]

def fill(word):
    print(word)
    for char in word:
        pyautogui.press(char)
    pyautogui.press('enter')
    time.sleep(1)

def start():
    pyautogui.click(start_pos)
    letters = get_text()
    print(letters)
    posibilities = get_posibilities(letters)
    print(posibilities)
    for word in posibilities:
        fill(word)

if __name__ == '__main__':
    start()
