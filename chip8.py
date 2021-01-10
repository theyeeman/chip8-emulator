class chip8:
    def __init__(self):
        pc = 0
        ir = 0 
        v = [0] * 16
        op = ""
        memory = [0] * 4096
        stack = [0] * 16
        delayTimer = 0
        soundTimer = 0

    def loadROM(self, file, offset):
        data = open(file, 'rb').read()
        for index, byte in enumerate(data):
            self.memory[index + offset] = byte

    
    
    
