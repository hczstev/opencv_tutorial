from cv2 import imshow, waitKey, destroyAllWindows
from os.path import abspath, join
from matplotlib import pyplot as plt

root_path = abspath("../")
data_path = join(root_path, "data")

messi_image = join(data_path, "messi5.jpg")
gradient_image = join(data_path, "gradient.png")
logo_image = join(data_path, "logo.png")


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
