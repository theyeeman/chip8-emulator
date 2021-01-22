from screen import chip8_Screen
from chip8 import chip8_Emulator
import pygame

if (__name__ == "__main__"):
    # Initalize all required variables
    myScreen = chip8_Screen(10)
    myScreen.initDisplay()
    cpu = chip8_Emulator(myScreen)

    # Load ROM here
    cpu.loadROM("ROM_Name.ch8", cpu.programMemoryStartAddress)

    while (cpu.running):

        clock = pygame.time.Clock()

        cpu.runOneCycle()
        cpu.screen.update()

        clock.tick(cpu.speed)
    
    pygame.quit()