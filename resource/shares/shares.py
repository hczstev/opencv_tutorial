from cv2 import imshow, waitKey, destroyAllWindows
from os.path import abspath, join
from matplotlib import pyplot as plt

root_path = abspath("../")

messi_image = join(root_path, "data", "messi5.jpg")
gradient_image = join(root_path, "data", "gradient.png")


def show_image(img):
    imshow('image', img)
    waitKey(0)
    destroyAllWindows()


def show_images(*imgs):
    num_col = 3
    num_row = (len(imgs) - 1) // num_col + 1

    for i, img in enumerate(imgs):
        plt.subplot(num_row, num_col, i + 1), plt.imshow(img["image"],"gray")
        plt.title(img["title"])
        plt.xticks([]), plt.yticks([])

    plt.ion()
    plt.waitforbuttonpress()
    plt.close()
