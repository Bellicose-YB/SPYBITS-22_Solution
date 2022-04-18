import cv2
import numpy as np

img1 = cv2.imread("Exclusive_yet_reversible\img1.jpeg")
img2 = cv2.imread("Exclusive_yet_reversible\img2.jpeg")
img3 = cv2.imread("Exclusive_yet_reversible\img3.jpeg")

# method 1
img12 = cv2.bitwise_xor(img2, img1)

final = cv2.bitwise_xor(img12, img3)

# method 2

final = img1^img2^img3

cv2.imwrite("Exclusive_yet_reversible\ans.jpeg", final)


cv2.imshow('BitwiseXOR', final)

cv2.waitKey(0)
cv2.destroyAllWindows()
