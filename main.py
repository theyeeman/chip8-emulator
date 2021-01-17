from screen import chip8_Screen
from chip8 import *
#from functions import *
import pygame
import sys

from pygame.locals import (
    K_1,
    K_2,
    K_3,
    K_4,
    K_q,
    K_w,
    K_e,
    K_r,
    K_a,
    K_s,
    K_d,
    K_f,
    K_z,
    K_x,
    K_c,
    K_v
)

if (__name__ == "__main__"):
    # Initalize all required variables
    myScreen = chip8_Screen(10)
    myScreen.initDisplay()
    cpu = chip8_CPU(myScreen)

    cpu.loadROM("keypad_test.ch8", 0x200)

    while (cpu.running):

        clock = pygame.time.Clock()

        cpu.runOneCycle()
        cpu.screen.update()
        #print("op: ", hex(cpu.op), "pc: ", hex(cpu.pc))

        clock.tick(60)
    
    pygame.quit()