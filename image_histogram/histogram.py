import cv2
import numpy as np
from matplotlib import pyplot as plt

img_path = "test.jpg"

img = cv2.imread(img_path, 0)
x = img.ravel()
plt.hist(x, 256, [0, 256])
plt.show()
