from PIL import ImageGrab
import pytesseract
import pyautogui

top_left = (410, 400)
bottom_right = (1371, 507)
seen_button = (820, 536)
new_button = (954, 537)
pyautogui.PAUSE = 0

def read_text(words):
    img = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    result = pytesseract.image_to_string(img, lang='eng', config='--psm 10').strip()
    if result in words:
        pyautogui.moveTo(seen_button[0], seen_button[1])
        pyautogui.click()
    else:
        pyautogui.moveTo(new_button[0], new_button[1])
        pyautogui.click()
        words.add(result)
    read_text(words)

if __name__ == '__main__':
    read_text(set())
