""" Configuration code for getting file path for ROM and getting emulator 
variables for clockspeed and screen scale.
"""

import easygui

def getEmulatorVariables():
    """Open up file selection window to select ROM and emulator variables."""
    filePath = easygui.fileopenbox()

    # Get emulator variables from user
    msg = "Enter CHIP-8 emulation variables"
    title = "CHIP-8 Setup"
    fieldNames = [
        "Clock Speed (Hz) (min 30, max 600)", 
        "Screen Scale Multiplier (min 1, max 20)",
        ]
    fieldValues = easygui.multenterbox(msg, title, fieldNames)

    while (True):
        if (fieldValues is None):
            break
        
        errmsg = ""
        for i in range(len(fieldNames)):
            if (fieldValues[i].strip() == ""):
                errmsg = (errmsg 
                + ('"%s" is a required field.\n\n' % fieldNames[i]))
            elif (not fieldValues[i].isdigit()):
                errmsg = (errmsg 
                        + ('"%s" contains non-number values.\n\n' 
                            % fieldNames[i]))

        if (errmsg == ""):
            break # No problems found

        fieldValues = easygui.multenterbox(
            errmsg, title, fieldNames, fieldValues)
    
    userClockSpeed = int(fieldValues[0])
    userScreenScale = int(fieldValues[1])

    # Bounds check for emulator variables
    userClockSpeed = max(30, min(userClockSpeed, 600))
    userScreenScale = max(1, min(userScreenScale, 20))
    
    return filePath, userClockSpeed, userScreenScale
