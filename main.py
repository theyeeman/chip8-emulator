from screen import chip8_Screen
#from chip8 import *
#from functions import *
import pygame
import sys

fontSet = {
    0 :[0xF0, 0x90, 0x90, 0x90, 0xF0],
    1 : [0x20, 0x60, 0x20, 0x20, 0x70],
    2 : [0xF0, 0x10, 0xF0, 0x80, 0xF0],
    3 : [0xF0, 0x10, 0xF0, 0x10, 0xF0],
    4 : [0x90, 0x90, 0xF0, 0x10, 0x10],
    5 : [0xF0, 0x80, 0xF0, 0x10, 0xF0],
    6 : [0xF0, 0x80, 0xF0, 0x90, 0xF0],
    7 : [0xF0, 0x10, 0x20, 0x40, 0x40],
    8 : [0xF0, 0x90, 0xF0, 0x90, 0xF0],
    9 : [0xF0, 0x90, 0xF0, 0x10, 0xF0],
    10 : [0xF0, 0x90, 0xF0, 0x90, 0x90],
    11 : [0xE0, 0x90, 0xE0, 0x90, 0xE0],
    12 : [0xF0, 0x80, 0x80, 0x80, 0xF0],
    13 : [0xE0, 0x90, 0x90, 0x90, 0xE0],
    14 : [0xF0, 0x80, 0xF0, 0x80, 0xF0],
    15 : [0xF0, 0x80, 0xF0, 0x80, 0x80]
    }

def testDraw(myscreen, num):
    if (num < 0 or num > 15):
        return None
    
    font = fontSet[num]

    row = 0
    column = 0

    for line in font:
        for _ in range(8):
            if (line & 1 == 1):
                myscreen.setPixel(row, column)
                print("setting pixel")
            line >> 1
            row = row + 1

        column = column + 1
        row = 0
    
    myscreen.update()

if (__name__ == "__main__"):
    # Initalize all required variables
    
    # Emulation loop
    #while(True):
        # Get keypress
        
        # Emulate one CPU cycle
        
        # Update graphics is drawing flag is set

    myScreen = chip8_Screen(10)
    myScreen.initDisplay()

    running = True

    # for i in range(8):
    #     font = fontSet[i]
    #     row = i * 8
    #     column = 1

    #     for line in font:
    #         print(bin(line))
    #         for _ in range(8):
    #             if (line & 0x80 == 0b10000000):
    #                 myScreen.setPixel(row, column)
    #                 print("setting pixel", row, column)
    #             line = (line << 1) & 0xFF
    #             print(line)
    #             row = row + 1

    #         column = column + 1
    #         row = i * 8
        
    # myScreen.update()

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        #myScreen.setPixel(10, 5)
        #myScreen.update()
        
    