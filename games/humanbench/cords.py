import pyautogui
import time

def get_current_cords():
    return pyautogui.position()

def main():
    while True:
        x, y = get_current_cords()
        print(x, y)
        time.sleep(.5)

if __name__ == '__main__':
    main()
