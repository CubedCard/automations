from PIL import ImageGrab
import pytesseract
import pyautogui

top_left = (909, 418)
bottom_right = (1754, 609)
pyautogui.PAUSE = 0
custom_oem_psm_config = r'--oem 3 --psm 6 -c tessedit_char_blacklist="|/[]{}"'

def read_text():
    img = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    result = pytesseract.image_to_string(img, lang='eng', config=custom_oem_psm_config).strip()
    words = result.split(' ')
    for word in words:
        word = word.strip()
        for char in word:
            if char == '\n':
                pyautogui.press('space')
                continue
            pyautogui.press(char)
        pyautogui.press('space')

if __name__ == '__main__':
    read_text()
