# Main program.
from screen import chip8_Screen
from chip8 import chip8_Emulator
import pygame
import config

if (__name__ == "__main__"):
    
    filePath, userClockSpeed, userScreenScale = config.getEmulatorVariables()
    
    # Initalize emulator
    myScreen = chip8_Screen(userScreenScale)
    myScreen.initDisplay()
    cpu = chip8_Emulator(myScreen, userClockSpeed)

    cpu.loadROM(filePath, cpu.programMemoryStartAddress)

    while (cpu.running):

        clock = pygame.time.Clock()

        cpu.runOneCycle()

        clock.tick(cpu.speed)
    
    pygame.quit()