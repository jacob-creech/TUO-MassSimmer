from PIL import ImageGrab
import os
import time
 
# 1085, 527
x_pad = 1084
y_pad = 526
# 2286, 1428 
 
def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1202, y_pad + 902)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()