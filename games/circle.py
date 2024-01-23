import pyautogui
import math
import time

time.sleep(1)
pyautogui.PAUSE = 0

radius = 250
center_x, center_y = 896, 606

num_points = 3
angle_increment = 2 * math.pi / num_points

for i in range(num_points + 1):
    pyautogui.mouseDown()
    x = int(center_x + radius * math.cos(i * angle_increment))
    y = int(center_y + radius * math.sin(i * angle_increment))

    pyautogui.moveTo(x, y)

pyautogui.mouseUp()
