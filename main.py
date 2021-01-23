from screen import chip8_Screen
from chip8 import chip8_Emulator
import pygame
import easygui

if (__name__ == "__main__"):
    # Open up file selection window to select ROM
    filePath = easygui.fileopenbox()

    # Get emulator variables from user
    msg = "Enter CHIP-8 emulation variables"
    title = "CHIP-8 Setup"
    fieldNames = ["Clock Speed (Hz) (min 30, max 600)", "Screen Scale (min 1, max 20)"]
    fieldValues = easygui.multenterbox(msg, title, fieldNames)

    while (True):
        if (fieldValues == None):
            break
        
        errmsg = ""
        for i in range(len(fieldNames)):
            if (fieldValues[i].strip() == ""):
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
            elif (not fieldValues[i].isdigit()):
                errmsg = errmsg + ('"%s" contains non-number values.\n\n' % fieldNames[i])

        if (errmsg == ""):
            break # No problems found

        fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
    
    userClockSpeed = int(fieldValues[0])
    userScreenScale = int(fieldValues[1])

    # Bounds check for emulator variables
    userClockSpeed = max(30, min(userClockSpeed, 600))
    userScreenScale = max(1, min(userScreenScale, 20))
    
    # Initalize emulator
    myScreen = chip8_Screen(userScreenScale)
    myScreen.initDisplay()
    cpu = chip8_Emulator(myScreen, userClockSpeed)

    # Load ROM here
    cpu.loadROM(filePath, cpu.programMemoryStartAddress)

    while (cpu.running):

        clock = pygame.time.Clock()

        cpu.runOneCycle()
        cpu.screen.update()

        clock.tick(cpu.speed)
    
    pygame.quit()