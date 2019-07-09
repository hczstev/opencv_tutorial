import numpy as np
import cv2
from shares.shares import *

def scaling(img):
    # interpolation is preferred to be cv2.INTER_AREA for shrinking
    #                                  cv2.INTER_CUBIC or cv2.INTER_LINEAR for zooming
    shrunk_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    h, w = img.shape[:2]
    zoomed_img = cv2.resize(img, (2*h, 2*w), interpolation=cv2.INTER_CUBIC)

    return shrunk_img, zoomed_img


def transform(img):
    th = 30
    rows, cols, _ = img.shape

    # transformation matrix
    # M = np.float32([[cos(th), -sin(th), dx],
    #                 [sin(th), cos(th), dy]])

    # 1. get M by cv2.getRotationMatrix2D
    rotation_center = (cols / 2, rows / 2)
    M = cv2.getRotationMatrix2D(rotation_center, th, 1)  # 2 * 3
    res = cv2.warpAffine(img, M, (cols, rows))
    # show_image(res)

    # 2. get M by three points affine transform
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)  # 2 * 3
    res = cv2.warpAffine(img, M, (cols, rows))
    # show_image(res)

    # 3. get M for perspective transform
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)  # 3 * 3
    res = cv2.warpPerspective(img, M, (300, 300))
    # show_image(res)


if __name__ == "__main__":
    img = cv2.imread(messi_image, cv2.IMREAD_COLOR)  # BGR
    scaling(img)
    transform(img)
