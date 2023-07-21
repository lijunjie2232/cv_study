from utils import *

def draw_circle(event, x, y, flags, params, **args):
    if event == cv.EVENT_LBUTTONUP:
        cv.circle(img, (x, y), 7, (253, 121, 168), -1)

class CaptureUtils:
    '''
    mode: 0-points 1-rectangle
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
            if self.click_down_ed and self.mode == 1:
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
        elif event == cv.EVENT_LBUTTONUP:
            if self.mode == 1:
                self.click_down_ed = False
                if self.x_0 == x or self.y_0 == y:
                    self.img = self.img_0.copy()
                else:
                    self.img_0 = self.img
                    self.collection.append(((self.x_0, self.y_0), (self.x_1, self.y_1)))

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
    c = CaptureUtils(img, 1)
    print(c.startCapture('q'))