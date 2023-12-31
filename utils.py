import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def showImage_cv(img: cv.Mat, text="", sec=-1, key='q', cvt=True):
    if cvt:
        cv.imshow(text, cv.cvtColor(img, cv.COLOR_RGB2BGR))
    else:
        cv.imshow(text, img)
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

def showImage(pic, title=None, axis=True, figsize=(5,5), cmap=None, cvt=False):
    if cvt:
        pic = cv.cvtColor(pic.copy(), cv.COLOR_RGB2BGR)
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

# xyxy2xywh and xywh2xyxy there are diff from yolo
#bbox(x1,y1,x2,y2)->bbox(x, y, w, h)
def xyxy2xywh(x:np.array):
    y = np.zeros_like(x)
    y[:, 0] = x[:, 0]
    y[:, 1] = x[:, 1]
    y[:, 2] = x[:, 2] - x[:, 0]
    y[:, 3] = x[:, 3] - x[:, 1]
    return y

#bbox(x, y, w, h)->bbox(x1,y1,x2,y2)
def xywh2xyxy(x:np.array):
    y = np.zeros_like(x)
    y[:, 0] = x[:, 0]
    y[:, 1] = x[:, 1]
    y[:, 2] = x[:, 0] + x[:, 2]
    y[:, 3] = x[:, 1] + x[:, 3]
    return y

def get_mean_std(dataset, type='train'):
    """
    计算数据集的均值和标准差
    :param type: 使用的是那个数据集的数据，有'train', 'test', 'testing'
    :return means: 均值
    :return stdevs: 标准差
    """
    num_imgs = len(dataset[type])
    for data in dataset[type]:
        img = data[0]
        for i in range(3):
            # 一个通道的均值和标准差
            means[i] += img[i, :, :].mean()
            stdevs[i] += img[i, :, :].std()


    means = np.asarray(means) / num_imgs
    stdevs = np.asarray(stdevs) / num_imgs

    print("{} : normMean = {}".format(type, means))
    print("{} : normstdevs = {}".format(type, stdevs))
    
    return means, stdevs