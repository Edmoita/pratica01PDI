import numpy as np
import cv2
import math as mt
#import tkinter

#le a imagem, coloca o nome aqui
def loadImg():
    img = cv2.imread('imagem.png', 0)
    return img

#Q1
def contrastStretching(img, t=135):
    one = img.shape[0]
    two = img.shape[1]

    new_img = np.copy(img)

    for i in range(one):
        for k in range(two):
            if(img[i][k] < t):
                new_img[i][k] = 0
            else:
                new_img[i][k] = 255
            #print(new_img[i][k])
            #new_img[i][k] = 1/(1 + (190/(img[i][k]))**mt.e)

    #cv2.imshow('image', new_img)
    return new_img

#Q2
def logarithmTransformation(img, c=1):
    one = img.shape[0]
    two = img.shape[1]

    new_img = np.copy(img)
    #cv2.imshow('original', new_img)
    for i in range(one):
        for k in range(two):
            new_image[i][k] = (c * mt.log10(1 + image[i, j]/255))*255

    return new_img


def linearization(minm, maxm, value):
    return 255 * value / maxm


#Q3
def gammaCorrection(img, y=1):
    c =1
    one = img.shape[0]
    two = img.shape[1]

    new_img = np.copy(img)

    for i in range(one):
        for k in range(two):
            new_img[i][k] = (c * (img[i][k]/255)**y)*255
            
    return new_img

#Q4
def bitsLayer(img, layer):
    one = img.shape[0]
    two = img.shape[1]
    new_value = []

    new_img = np.copy(img)

    for i in range(one):
        for k in range(two):
            binValue = format(img[i][k], '08b')
            if binValue[8 - layer] == '0':
                new_img[i][k] = 0
            else:
                new_img[i][k] = 255


    #cv2.imshow('image', new_img)
    return new_img

"""tentativa de um alargamento de contraste para imagens de raio x
não funciona bem em raio x, mas fica melhor que o "alargamento" da
questão 1"""
#Q5
def imgCorrection(img, c, d):
    one = img.shape[0]
    two = img.shape[1]
    new_value = []

    new_img = np.copy(img)

    for i in range(one):
        for k in range(two):
            new_img[i][k] = (img[i][k] - c)*(255/(d - c))



    return new_img
'''
img = imgCorrection(loadImg(),65,197)
cv2.imshow('image', img)

#cv2.imshow('image', contrastStretching(loadImg()))
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
