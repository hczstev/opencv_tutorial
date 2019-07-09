from cv2 import imshow, waitKey, destroyAllWindows


def show_image(img):
    imshow('image', img)
    waitKey(0)
    destroyAllWindows()
