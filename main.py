# Main program.
from screen import chip8_Screen
from chip8 import chip8_Emulator
import pygame
import config

if (__name__ == "__main__"):
    
    #filePath, userClockSpeed, userScreenScale = config.getEmulatorVariables()
    filePath = "C:\\repos\\chip8-emulator\\ROMs\\keypad_test.ch8"
    userClockSpeed = 30
    userScreenScale = 10

    # Initalize emulator
    screen = chip8_Screen(userScreenScale)
    screen.initDisplay()
    cpu = chip8_Emulator(screen, userClockSpeed)

    cpu.loadROM(filePath, cpu.programMemoryStartAddress)

    while (cpu.running):

        clock = pygame.time.Clock()

        cpu.runOneCycle()
        print('op: ', hex(cpu.op), 'pc: ', hex(cpu.pc))

        clock.tick(cpu.speed)
    
    pygame.quit()