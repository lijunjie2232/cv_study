import cv2 as cv
import numpy as np

def showImage(text, img: cv.Mat, sec=0, key=None, cvt=True):
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
        
def saveImage(fileName, img:cv.Mat, cvt=True):
    if cvt:
        cv.imwrite(fileName, cv.cvtColor(img, cv.COLOR_RGB2BGR))
    else:
        cv.imwrite(fileName, img)