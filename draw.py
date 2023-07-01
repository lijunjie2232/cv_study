from utils import *

def draw_circle(event, x, y, flags, **args):
    if event == cv.EVENT_LBUTTONUP:
        cv.circle(img, (x, y), 100, (253, 121, 168), -1)

if __name__ == '__main__':
    img = np.ones((500, 500, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while(1):
        if not showImage('image', img, key='q'):
            break
    cv.destroyAllWindows()