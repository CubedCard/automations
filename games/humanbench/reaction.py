import pyautogui
from PIL import ImageGrab
import keyboard 
import sys

def is_pixel_green(x, y):
    pixel_color = ImageGrab.grab(bbox=(x, y, x+1, y+1)).getpixel((0, 0))

    # check if pixel is green
    is_green = pixel_color[1] > pixel_color[0] and pixel_color[1] > pixel_color[2]

    return is_green

def main():
    try:
        x, y = pyautogui.position()

        if is_pixel_green(x, y):
            pyautogui.click()

    except Exception as e:
        print(f"An error occurred: {e}") 
        sys.exit(1)

if __name__ == "__main__":
    pyautogui.PAUSE = 0
    while not keyboard.is_pressed('q'):
        main()
