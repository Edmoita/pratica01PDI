import numpy as np
import math as mt

# Q1
def contrastStretching(img, threshold, E):
    height = img.shape[0]
    width = img.shape[1]

    new_img = np.copy(img)

    for i in range(height):
        for j in range(width):
            new_img[i][j] = 255* (1/(1 + (threshold/(img[i][j]/255))**E))

    return new_img

# Q1 - Alternativa
def imgCorrection(img, new_min, new_max):
    height = img.shape[0]
    width = img.shape[1]

    new_img = np.copy(img)

    for i in range(height):
        for j in range(width):
            new_img[i][j] = (img[i][j] - new_min)*(255/(new_max - new_min))

    return new_img

# Q2
def logarithmTransformation(img, c=1):
    height = img.shape[0]
    width = img.shape[1]

    new_img = np.copy(img)

    for i in range(height):
        for j in range(width):
            new_img[i][j] = (c * mt.log10(1 + img[i][j]/255))*255

    return new_img

# Q3
def gammaCorrection(img, y, c=1):
    height = img.shape[0]
    width = img.shape[1]

    new_img = np.copy(img)

    for i in range(height):
        for j in range(width):
            new_img[i][j] = (c * (img[i][j]/255)**y)*255

    return new_img

# Q4
def bitsLayer(img, layer):
    height = img.shape[0]
    width = img.shape[1]

    new_img = np.copy(img)

    for i in range(height):
        for j in range(width):
            binValue = format(img[i][j], '08b')
            if binValue[8 - layer] == '0':
                new_img[i][j] = 0
            else:
                new_img[i][j] = 255

    return new_img


# Q5
def imgNegative(img):
    height = img.shape[0]
    width = img.shape[1]

    new_img = np.copy(img)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = 255 - img[i][j]

    return new_img
