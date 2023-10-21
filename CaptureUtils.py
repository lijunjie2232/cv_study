from typing import Any
from utils import *

def draw_circle(event, x, y, flags, params, **args):
    if event == cv.EVENT_LBUTTONUP:
        cv.circle(img, (x, y), 7, (253, 121, 168), -1)

class CaptureUtils:
    '''
    @params img: img to be show
    @params mode:  
                    0-points
                    1-rectangle
                    2-line
    '''
    originalImage = None
    x_0 = 0
    x_1 = 0
    y_0 = 0
    y_1 = 0
    mode = 0
    color = (253, 121, 168)
    click_down_ed = False
    collection = None
    def __init__(self, img:cv.Mat, mode=0, color=(253, 121, 168)):
        self.originalImage = img
        self.img_0 = self.originalImage.copy()
        self.img = self.originalImage.copy()
        self.color = color
        self.mode = mode
        
    def getter(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.x_0 = x
            self.y_0 = y
            self.click_down_ed = True
        elif event == cv.EVENT_LBUTTONDBLCLK:
            if self.mode == 0:
                cv.circle(self.img_0, (x, y), 5, self.color, -1)
                self.click_down_ed = False
                if (x, y) not in self.collection:
                    self.collection.append((x, y))
        elif event == cv.EVENT_MOUSEMOVE:
            if self.mode == 1:
                if self.click_down_ed:
                    self.x_1 = x
                    self.y_1 = y
                    self.img = self.img_0.copy()
                    # cv.rectangle(img, (x_0, y_0), (x_1, y_1), self.color, -1)
                    cv.line(self.img, (self.x_0, self.y_0), (self.x_0, self.y_1), self.color, 1)
                    cv.line(self.img, (self.x_0, self.y_1), (self.x_1, self.y_1), self.color, 1)
                    cv.line(self.img, (self.x_1, self.y_1), (self.x_1, self.y_0), self.color, 1)
                    cv.line(self.img, (self.x_1, self.y_0), (self.x_0, self.y_0), self.color, 1)
            else:
                self.img = self.img_0.copy()
                cv.line(self.img, (x-5, y), (x+5,y), self.color, 1)
                cv.line(self.img, (x, y-5), (x,y+5), self.color, 1)
                if self.mode == 2:# and not self.click_down_ed:
                    self.draw_line(x, y)
        elif event == cv.EVENT_LBUTTONUP:
            self.click_down_ed = False
            if self.mode == 1:
                if self.x_0 == x or self.y_0 == y:
                    self.img = self.img_0.copy()
                else:
                    self.img_0 = self.img
                box = self.formBox(((self.x_0, self.y_0), (self.x_1, self.y_1)))
                self.collection.append(box)
            if self.mode == 2:
                self.img = self.img_0.copy()
                if self.collection:
                    self.draw_line(x, y, draw_close=False)
                self.collection.append((x, y))
                self.img_0 = self.img
                self.x_0 = x
                self.y_0 = y

    def draw_line(self, x, y, draw_close=True):
        if self.collection:
            cv.line(self.img, self.collection[-1], (x,y), self.color, 1)
            if draw_close:
                cv.line(self.img, self.collection[0], (x,y), self.color, 1)
    
    def formBox(self, box):
        x = np.array((box[0][0], box[1][0]))
        y = np.array((box[0][1], box[1][1]))
        x.sort()
        y.sort()
        return ((x[0], y[0]), (x[1], y[1]))

    def startCapture(self, key='q'):
        self.collection = []
        cv.namedWindow('image')
        cv.setMouseCallback('image', self.getter)
        while(1):
            cv.imshow('image',self.img)
            if cv.waitKey(1) == ord(key):
                break
        cv.destroyAllWindows()
        return self.collection
    
    def __call__(self,  key='q'):
        return self.startCapture(key)

if __name__ == '__main__':
    # img = np.ones((500, 500, 3), np.uint8)*255
    # cv.namedWindow('image')
    # cv.setMouseCallback('image', draw_circle)
    # while(1):
    #     cv.imshow('image',img)
    #     if cv.waitKey(1) == ord('q'):
    #         break
    # cv.destroyAllWindows()
    img = np.ones((500, 500, 3), np.uint8)*255
    c = CaptureUtils(img, 2)
    print(c('q'))