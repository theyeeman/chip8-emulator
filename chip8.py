class chip8:
    def __init__(self):
        pc = 0 # Program counter
        ir = 0 # Index Register
        v = [0] * 16 # CPU Registers
        op = 0x0 # Current Opcode
        sp = 0 # Stack pointer
        keyPressed = 0
        memory = [0] * 4096
        stack = [0] * 16
        delayTimer = 0
        soundTimer = 0

    def loadROM(self, file, offset):
        data = open(file, 'rb').read()
        for index, byte in enumerate(data):
            self.memory[index + offset] = byte
            
    def getKeyPress(self):
        #something
            
    def fetch(self):
        self.op = memory[pc] << 8 |memory[pc + 1]
        pc += 2
        
    def decode(self):
        # need to parse opcode to see which one it  is
        # maybe stuff opcode instructions here? Or create a dictionary of opcodes that can be 
        # used for figuring out which opcode to execute
        # maybe just use decode func for parsing the opcode and then call execute func
        
        msd = self.op >> 12
        lsd = self.op & 0x000F
        lsd2 = (self.op & 0x00F0) >> 4
        
        if (msd == 0):
            if (lsd == 0):
                # 00E0 - CLS. Clear display
            else:
                # 00EE - RET. Return from subroutine. Set PC to top of stack, then decrement SP
        if (msd == 1):
            # 1nnn - JP addr. Set PC to nnn
        if (msd == 2):
            # 2nnn - CALL addr. Increment SP, push current PC to stack, then set PC to nnn
        if (msd == 3):
            # 3xkk - SE Vx, byte. Skip next instruction if Vx == kk (increase PC by 2)
        if (msd == 4):
            # 4xkk - SNE Vx, byte. Skip next instruction if Vx != kk (increase PC by 2)
        if (msd == 5):
            # 5xy0 - SE Vx, Vy. Skip next instruction if Vx == Vy (increase PC by 2)
        if (msd == 6):
            # 6xkk - LD Vx, byte. Set Vx = kk
        if (msd == 7):
            # 7xkk - ADD vx, byte. Set Vx = Vx + kk
        if (msd == 8):
            if (lsd == 0):
                # 8xy0 - LD Vx, Vy. Set Vx = Vy
            if (lsd == 1):
                # 8xy1 - OR Vx, Vy. Set Vx = Vx OR Vy
            if (lsd == 2):
                # 8xy2 - AND Vx, Vy. Set Vx = Vx AND Vy
            if (lsd == 3):
                # 8xy3 - XOR Vx, Vy. Set Vx = Vx XOR Vy
            if (lsd == 4):
                # 8xy4 - ADD Vx, Vy. Set Vx = Vx + Vy, set Vf = carry
            if (lsd == 5):
                # 8xy5 - SUB Vx, Vy. Set Vx = Vx - Vy, set Vf = NOT borrow
            if (lsd == 6):
                # 8xy6 - SHR Vx {, Vy}. Set Vx = Vx SHR 1. If lsb of Vx is 1, then Vf = 1, else Vf = 0. Then Vx = Vx \ 2
            if (lsd == 7):
                # 8xy7 - SUBN Vx, Vy. Set Vx = Vy - Vx, set Vf = NOT borrow
            if (lsd == E):
                # 8xyE - SHL Vx {, Vy}. Set Vx = Vx SHL 1. If msb of Vx is 1, then Vf = 1, else 0. Then Vx = Vx * 2
        if (msd == 9):
            # 9xy0 - SNE Vx, Vy. Skip next instruction if Vx != Vy (increase PC by 2)
        if (msd == 0xA):
            # Annn - Ld I, addr. Set IR = nnn
        if (msd == 0xB):
            # Bnnn - Jp V0, addr. Set PC = V0 + nnn
        if (msd == 0xC):
            # Cxkk - RND Vx, byte. Set Vx = random byte [0, 255] AND kk
        if (msd == 0xD):
            # Dxyn - DRW Vx, Vy, nibble. Display n-byte sprite starting at mem location IR at (Vx, Vy), set Vf = collision
        if (msd == 0xE):
            if (lsd == 0xE):
                # Ex9E - SKP Vx. If key pressed on keyboard corresponds with value in Vx, increment PC by 2
            if (lsd == 0x1):
                # ExA1 - SKNP Vx. If key not pressed on keyboard corresponds to value in Vx, increment PC by 2
        if (msd == 0xF):
            if (lsd2 == 0x0):
                if (lsd == 0x7):
                    # Fx07 LD Vx, DT. Set Vx = delay timer value
                if (lsd == 0xA):
                    # Fx0A - LD Vx, key. Store value of key press in Vx. All exeution is stopped until key is pressed.
            if (lsd2 === 0x1):
                if (lsd == 0x5):
                    # Fx15 - LD DT, Vx. Set delay timer = Vx
                if (lsd == 0x8):
                    # Fx18 - LD ST, Vx. Set sound timer = Vx
                if (lsd == 0xE):
                    # Fx1E - Add I, Vx. Set IR = IR + Vx
            if (lsd2 == 0x2):
                # Fx29 - LD F, Vx. Set IR = location of spite for digit Vx
            if (lsd2 == 0x3):
                # Fx33 - LD B, Vx. Store BCD represention of Vx in mem location IR, IR+1, and I+2
            if (lsd2 == 0x5):
                # Fx55 - LD [I], Vx. Store registers V0 to Vx in mem location starting at IR
            if (lsd2 == 0x6):
                # Fx65 - LD Vx, [I]. Read registers V0 to Vx from mem location starting at IR
        
                
    def execute(self):
        # Look up in dictionary

    def updateTimers(self):
        # update timer stuff here
        
    def runOneCycle(self):
        fetch()
        decode()
        updateTimers()
        
        
        
        

    
    
    
