from graphics import *
from chip8 import *
from functions import *



def fillScreenTest():
    win = GraphWin("test", 640, 320, )
    win.setCoords(0,0,64,32)

    for i in range(64):
        for j in range (32):
            a = Rectangle(Point(i, j), Point (i + 1, j + 1))
            a.draw(win)

    win.getMouse()
    win.close()


if (__name__ == "__main__"):
    cpu = chip8()

    while(1):
        print(hexToInt(getKey()))
