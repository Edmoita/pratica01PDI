import cv2
from PIL import ImageTk, Image

def load_image2(filename):
    image = cv2.imread(filename)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def convert_image_opencv_to_tk(opencv_image):
    im = Image.fromarray(opencv_image)
    im = resize_image(im)
    tk_image = ImageTk.PhotoImage(im)
    return tk_image

def convert_image_filename_to_tk(filename):
    img = Image.open(filename)
    img = resize_image(img)
    tk_image = ImageTk.PhotoImage(img)
    return tk_image

def resize_image(image):
    width, height = image.size
    ratio = height/width
    width = 400
    height = int(width * ratio)
    im = image.resize((width, height), Image.ANTIALIAS)
    return im
