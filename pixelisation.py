import cv2
import numpy as np

img_input = cv2.imread('input/cat.jpg')
# cv2.imshow("Input", img_input)

# print(img_input.shape)
height, width = img_input.shape[:2]
# print(width, height)

pixel_size =
new_width, new_height = (width // pixel_size, height // pixel_size)
# print(new_width, new_height)

img_temp = cv2.resize(img_input, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
img_output = cv2.resize(img_temp, (width, height), interpolation=cv2.INTER_NEAREST)
# cv2.imshow("Output", img_output)
# cv2.imwrite('output/cat.jpg', img_output)

img_hor = np.hstack((img_input, img_output))
cv2.imshow("Horizontal", img_hor)

cv2.waitKey(0)