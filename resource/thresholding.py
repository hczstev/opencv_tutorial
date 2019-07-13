import cv2
from shares import *


def trunc_thresh(img):
    _, res = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    show_image(res)


def simple_thresh(img):
    images = [{"title": "origin", "image": img}]
    thresh_stypes = [
        "THRESH_BINARY",
        "THRESH_BINARY_INV",
        "THRESH_TRUNC",
        "THRESH_TOZERO",
        "THRESH_TOZERO_INV",
    ]

    for style in thresh_stypes:
        if hasattr(cv2, style):
            _, res = cv2.threshold(img, 127, 255, getattr(cv2, style))
            images.append(
                {
                    "title": style,
                    "image": res,
                }
            )

    show_images(*images)


if __name__ == "__main__":
    img = cv2.imread(gradient_image, cv2.IMREAD_GRAYSCALE)  # BGR

    trunc_thresh(img)
    simple_thresh(img)


