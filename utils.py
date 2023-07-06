import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def showImage_cv(text, img: cv.Mat, sec=0, key='q', cvt=True):
    if cvt:
        cv.imshow("", cv.cvtColor(img, cv.COLOR_RGB2BGR))
    else:
        cv.imshow("", img)
    if key:
        if cv.waitKey(sec) == ord(key):
            cv.destroyAllWindows()
    else:
        cv.waitKey(sec)
        cv.destroyAllWindows()
    return 0
        
def saveImage_cv(fileName, img:cv.Mat, cvt=True):
    if cvt:
        cv.imwrite(fileName, cv.cvtColor(img, cv.COLOR_RGB2BGR))
    else:
        cv.imwrite(fileName, img)
        
def readImage_cv(imgPath:str):
    return cv.cvtColor(cv.imread(imgPath), cv.COLOR_BGR2RGB)

def showImage(pic, title=None, axis=True, figsize=(5,5), cmap=None):
    plt.figure(figsize=figsize)
    plt.imshow(pic, cmap=cmap)
    plt.axis(axis)
    if title:
        plt.title(title)
    plt.show()
    
def readImage(url:str):
    if not os.path.isfile(url):
        raise(Exception("input must exist and should be file url instead of director"))
    image = cv.imread(url)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image

def saveImage(image:np.array, url:str, cvt=True):
    dir = os.path.dirname(url)
    if not os.path.isdir(dir):
        os.makedirs(dir)
    if cvt:
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    cv.imwrite(url, image)