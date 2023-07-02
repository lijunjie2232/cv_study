from utils import *

def draw_circle(event, x, y, flags, params, **args):
    if event == cv.EVENT_LBUTTONUP:
        cv.circle(img, (x, y), 7, (253, 121, 168), -1)

if __name__ == '__main__':
    img = np.ones((500, 500, 3), np.uint8)*255
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while(1):
        cv.imshow('image',img)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()