import sys
import pyautogui
import time

def print_pins(length):
    if length == 1:
        return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    else:
        return [str(i) + j for i in range(10) for j in print_pins(length - 1)]

if __name__ == '__main__':
    pyautogui.PAUSE = 0
    time.sleep(3)
    length = int(sys.argv[1])
    pins = [pin for pin in print_pins(length)]
    for pin in pins:
        for char in pin:
            pyautogui.press(char)
        pyautogui.press('enter')
        time.sleep(0.5)

