from PIL import ImageGrab
import numpy as np

top_left = (1138, 302)
bottom_right = (1532, 694)

screenshot = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
screenshot_array = np.array(screenshot)

square_color = [60, 116, 187, 255]
background_color = [70, 135, 203, 255]

num_squares = 0

for row in range(screenshot_array.shape[0]):
    if num_squares > 0:
        break
    for col in range(screenshot_array.shape[1] - 1):
        pixels, pixels_next = list(screenshot_array[row, col]), list(screenshot_array[row, col + 1])
        if all(abs(p1 - p2) <= 4 for p1, p2 in zip(pixels, square_color)) and all(abs(p1 - p2) <= 3 for p1, p2 in zip(pixels_next, background_color)):
            num_squares += 1

total_squares = num_squares * num_squares

print(f"The number of squares in a row of the grid is: {num_squares}")
print(f"The total number of squares in the grid is: {total_squares}")
