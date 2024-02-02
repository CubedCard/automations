import pyautogui
from PIL import ImageGrab
import pytesseract

top_left = (1032, 520)
bottom_right = (1299, 597)

input_box = (1327, 582)
start_button = (1329, 615)

pyautogui.PAUSE = 0

def get_question():
    screenshot = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    question = pytesseract.image_to_string(screenshot, lang='eng', config='--oem 3 -c tessedit_char_whitelist=0123456789x= --dpi 70')
    return question

def click_start():
    pyautogui.moveTo(start_button[0], start_button[1])
    pyautogui.click()
    pyautogui.click()

def solve_question(question):
    question = question.replace("x", "*")
    question = question.replace("=", "")
    question = question.replace(" ", "")
    question = question.replace("?", "")
    if question[-1] == "*":
        question = "7*11"
    return eval(question)

def input_answer(answer):
    pyautogui.moveTo(input_box[0], input_box[1])
    pyautogui.click()
    pyautogui.typewrite(str(answer))

if __name__ == "__main__":
    click_start()
    for i in range(1000):
        question = get_question().strip()
        answer = solve_question(question)
        print(question, answer)
        input_answer(answer)
