import cv2
from PIL import ImageTk, Image

def load_opencv_image(filename):
    opencv_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    return opencv_image

def convert_image_opencv_to_tk(opencv_image):
    im = Image.fromarray(opencv_image)
    im = resize_image(im)
    tk_image = ImageTk.PhotoImage(im)
    return tk_image

def resize_image(image):
    width, height = image.size
    ratio = height/width
    width = 400
    height = int(width * ratio)
    im = image.resize((width, height), Image.ANTIALIAS)
    return im
