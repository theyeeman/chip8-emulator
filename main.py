from graphics import *
from chip8 import *
from functions import *
import pygame
import sys

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
    pygame.init()
    screen = pygame.display.set_mode((640,480))

    white = (255, 255, 255)
    black = (0, 0, 0)

    screen.fill(white)

    pygame.draw.rect(screen, black, (200,150,100,50))

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            print(hexToInt(getKey()))
            pygame.display.update()
