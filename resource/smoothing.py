import cv2
from shares import *


if __name__ == "__main__":
    img = cv2.imread(logo_image)

    # Averaging
    img = cv2.blur(img, (5, 5))

    # Gaussian Filtering
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # Median Filtering
    median = cv2.medianBlur(img, 5)  # Remove noise

    # Bilateral Filtering
    blur = cv2.bilateralFilter(img, 9, 75, 75)  # Keep edge and remove noise
