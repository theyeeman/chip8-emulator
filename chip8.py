class chip8:
    def __init__(self):
        pc = 0
        ir = 0 
        v = [0] * 16
        op = 0x0
        memory = [0] * 4096
        stack = [0] * 16
        delayTimer = 0
        soundTimer = 0

    def loadROM(self, file, offset):
        data = open(file, 'rb').read()
        for index, byte in enumerate(data):
            self.memory[index + offset] = byte
            
    def fetch(self):
        op = memory[pc]
        
    def decode(self):
        # need to parse opcode to see which one it  is
        # maybe stuff opcode instructions here? Or create a dictionary of opcodes that can be 
        # used for figuring out which opcode to execute
        # maybe just use decode func for parsing the opcode and then call execute func
        
    def execute(self):
        # Look up in dictionary
    
    def updateTimers(self):
        # update timer stuff here
        
    def runOneCycle(self):
        fetch()
        decode()
        updateTimers()
        
        
        
        

    
    
    
