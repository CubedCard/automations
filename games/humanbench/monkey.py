import cv2
from PIL import ImageGrab
import numpy as np
import pytesseract
import pyautogui

top_left = (1000, 193)
bottom_right = (1888, 715)
custom_oem_psm_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist="0123456789"'

screenshot = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > 100]
filtered_contours.sort(key=lambda c: cv2.boundingRect(c)[0])

number_positions = {i: [] for i in range(1, len(filtered_contours) + 1)}

for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    
    padding = 20
    roi = gray[y - padding:y + h + padding, x - padding:x + w + padding]
    number_text = pytesseract.image_to_string(roi, config=custom_oem_psm_config)

    number_positions[int(number_text.strip())].append((x, y))

number_positions = dict(sorted(number_positions.items()))

for number in list(number_positions.keys()):
    positions = number_positions[number]
    if len(positions) > 1:
        for position in positions:
            for other_number in list(number_positions.keys()):
                if other_number != number:
                    other_positions = number_positions[other_number]
                    for other_position in other_positions:
                        if abs(position[0] - other_position[0]) < 30 and abs(position[1] - other_position[1]) < 30:
                            number_positions[number].remove(position)
                            break

print(len(number_positions), number_positions.keys())
print(number_positions)

for number in list(number_positions.keys()):
    positions = number_positions[number]
    if len(positions) > 0:
        pyautogui.moveTo(top_left[0] + positions[0][0], top_left[1] + positions[0][1])
        pyautogui.click()
