import pyautogui
import keyboard

def click_cookie():
    pyautogui.click()

if __name__ == "__main__":
    pyautogui.PAUSE = 0.001
    while True:
        click_cookie()
        if keyboard.is_pressed('q'):
            break
