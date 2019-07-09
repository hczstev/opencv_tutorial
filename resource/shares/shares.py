from cv2 import imshow, waitKey, destroyAllWindows
from os.path import abspath, join

root_path = abspath("../")
messi_image = join(root_path, "data", "messi5.jpg")
print(messi_image)


def show_image(img):
    imshow('image', img)
    waitKey(0)
    destroyAllWindows()
