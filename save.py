"""Class for handling save state."""

class Chip8SaveState():
    def __init__(self):
        """Initialize a save state instance. The class variables are nearly the 
        same as the main emulator class, however this class also keeps track
        of the screen.
        """
        self.saveStateValid = False
        self.pc = 0  # Program counter
        self.ir = 0  # Index Register
        self.v = []  # CPU Registers
        self.op = 0x0  # Current Opcode
        self.sp = 0  # Stack pointer
        self.programMemoryStartAddress = 0
        self.keyPressed = -1
        self.memory = []
        self.stack = []
        self.delayTimer = 0
        self.soundTimer = 0
        self.running = True
        self.beepFreq = 0
        self.beepDuration = 0
        self.speed = 0
        self.screen = []
        
    def saveSaveState(self, cpu):
        """Save a copy of the current emulator object and save the current
        screen drawing.
        """
        self.saveStateValid = True
        self.pc = cpu.pc  # Program counter
        self.ir = cpu.ir  # Index Register
        self.v = cpu.v.copy()  # CPU Registers
        self.op = cpu.op  # Current Opcode
        self.sp = cpu.sp  # Stack pointer
        self.programMemoryStartAddress = cpu.programMemoryStartAddress
        self.keyPressed = cpu.keyPressed
        self.memory = cpu.memory.copy()
        self.stack = cpu.stack.copy()
        self.delayTimer = cpu.delayTimer
        self.soundTimer = cpu.soundTimer
        self.running = cpu.running
        self.beepFreq = cpu.beepFreq
        self.beepDuration = cpu.beepDuration
        self.speed = cpu.speed

        cpu.screen.getPixelMap()
        self.screen = cpu.screen.pixelMap

    def loadSaveState(self, cpu):
        """Load the saved copy of the emulator object back into the emulator. 
        If there is currently no state saved, then calling this function does
        nothing.
        """
        if (self.saveStateValid):
            cpu.pc = self.pc # Program counter
            cpu.ir = self.ir # Index Register
            cpu.v = self.v.copy() # CPU Registers
            cpu.op = self.op # Current Opcode
            cpu.sp = self.sp # Stack pointer
            cpu.programMemoryStartAddress = self.programMemoryStartAddress
            cpu.keyPressed = self.keyPressed
            cpu.memory = self.memory.copy()
            cpu.stack = self.stack.copy()
            cpu.delayTimer = self.delayTimer
            cpu.soundTimer = self.soundTimer
            cpu.running = self.running
            cpu.beepFreq = self.beepFreq
            cpu.beepDuration = self.beepDuration
            cpu.speed = self.speed
            self._drawSaveScreen(cpu)

    def isSaveStateValid(self):
        """Returns if there is a stored save state."""
        return self.saveStateValid

    def _drawSaveScreen(self, cpu):
        # Draw the saved screen.
        cpu.screen.clearScreen()

        for y in range(32):
            for x in range(64):
                if (cpu.screen.pixelMap[y][x] == 1):
                    cpu.screen.setPixel(x, y)