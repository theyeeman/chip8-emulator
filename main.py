from screen import chip8_Screen
from chip8 import chip8_Emulator
import pygame
import easygui

if (__name__ == "__main__"):
    # Open up file selection window to select ROM
    filePath = easygui.fileopenbox()
    
    # Initalize emulator
    myScreen = chip8_Screen(10)
    myScreen.initDisplay()
    cpu = chip8_Emulator(myScreen)

    # Load ROM here
    cpu.loadROM(filePath, cpu.programMemoryStartAddress)

    while (cpu.running):

        clock = pygame.time.Clock()

        cpu.runOneCycle()
        cpu.screen.update()

        clock.tick(cpu.speed)
    
    pygame.quit()