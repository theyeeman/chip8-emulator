"""Main program."""

import pygame
import config
from screen import Chip8Screen
from chip8 import Chip8Emulator

if (__name__ == "__main__"):
    
    filePath, userClockSpeed, userScreenScale = config.getEmulatorVariables()

    # Initalize emulator
    screen = Chip8Screen(userScreenScale)
    screen.initDisplay()
    cpu = Chip8Emulator(screen, userClockSpeed)

    cpu.loadROM(filePath, cpu.programMemoryStartAddress)

    while (cpu.running):
        clock = pygame.time.Clock()
        cpu.runOneCycle()
        clock.tick(cpu.speed)
    pygame.quit()