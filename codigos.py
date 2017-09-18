import cv2
import numpy as np
from math import log10, log

def show_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Questao 01
''' s = T(r) = 1/(1 + (k/r)^E)'''

def load_image2(filename):
    image = cv2.imread(filename)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def contrast_stretching(image, threshold):
    height = image.shape[0]
    width = image.shape[1]
    new_image = image.copy()
    for i in range(height):
        for j in range(width):
            if image[i, j] < threshold:
                new_image[i, j] = 0
            else:
                new_image[i, j] = 255
    return new_image

# Questao 02
def logarithmic_transformation(image, constant=1):
    height = image.shape[0]
    width = image.shape[1]
    new_image = image.copy()
    for i in range(height):
        for j in range(width):
            new_image[i, j] = constant * log10(1 + image[i, j])
    return new_image


# Questao 03
def power_law_transformation(image, gamma, constant=1):
    height = image.shape[0]
    width = image.shape[1]
    new_image = image.copy()
    for i in range(height):
        for j in range(width):
            new_image[i, j] = constant * (image[i, j]**gamma)
    return new_image

def bit_is_active(rate, levels, bit):
    binary_rate = bin(rate)[2:].zfill(levels)
    is_active = int(binary_rate[levels - bit - 1])
    return is_active

# Questao 04
def bit_plane_slicing(image, bit_plane):
    levels = 8
    height = image.shape[0]
    width = image.shape[1]
    new_image = image.copy()
    for i in range(height):
        for j in range(width):
            if bit_is_active(image[i, j], levels, bit_plane):
                new_image[i, j] = 255
            else:
                new_image[i, j] = 0
    return new_image

# Questao 05
def image_negative(image):
    height = image.shape[0]
    width = image.shape[1]
    new_image = image.copy()
    for i in range(height):
        for j in range(width):
            new_image[i, j] = 255 - image[i, j]
    return new_image

def intensity_level_slicing(image, a, b):
    height = image.shape[0]
    width = image.shape[1]
    new_image = image.copy()
    for i in range(height):
        for j in range(width):
            if image[i, j] >= a and image[i, j] <= b:
                new_image[i, j] = 255
            else:
                new_image[i, j] = image[i, j]
    return new_image

'''
image = cv2.imread('resources/100.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

new_image = contrast_stretching(gray_image, 127)
show_image('contrast_stretching', new_image)

new_image = logarithmic_transformation(gray_image, 50)
show_image('logarithmic_transformation', new_image)

new_image = power_law_transformation(gray_image, 4)
show_image('power_law_transformation', new_image)

for i in range(0, 8):
    new_image = bit_plane_slicing(gray_image, i)
    show_image('bit_plane_slicing_' + str(i), new_image)

new_image = image_negative(gray_image)
show_image('image_negative', new_image)

new_image = intensity_level_slicing(gray_image, 70, 230)
show_image('intensity_level_slicing', new_image)
'''
