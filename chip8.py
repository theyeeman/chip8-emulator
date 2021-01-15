# Opcode information from http://devernay.free.fr/hacks/chip8/C8TECH10.HTM
import random

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
        key = -1

        #get key pressed and set it to key

        return key
            
    def fetch(self):
        self.op = memory[pc] << 8 | memory[pc + 1]
        pc += 2
        
    def decode(self):
        # need to parse opcode to see which one it  is
        # maybe stuff opcode instructions here? Or create a dictionary of opcodes that can be 
        # used for figuring out which opcode to execute
        # maybe just use decode func for parsing the opcode and then call execute func
        
        # 0x[msd][x][y][lsd]
        msd = self.op >> 12
        x = (self.op & 0x0F00) >> 8
        y = (self.op & 0x00F0) >> 4
        lsd = self.op & 0x000F

        kk = self.op & 0x00FF
        nnn = self.op & 0x0FFF
        
        if (msd == 0):
            if (lsd == 0):
                # 00E0 - CLS. Clear display
                pass

            else:
                # 00EE - RET. Return from subroutine. Set PC to top of stack, then decrement SP
                pass

        if (msd == 0x1):
            # 1nnn - JP addr. Set PC to nnn
            self.pc = nnn

        if (msd == 0x2):
            # 2nnn - CALL addr. Increment SP, push current PC to stack, then set PC to nnn
            self.sp += 1
            self.stack.push(self.pc)
            self.pc = nnn

        if (msd == 0x3):
            # 3xkk - SE Vx, byte. Skip next instruction if Vx == kk (increase PC by 2)
            if (self.v[x] == kk):
                self.pc += 2

        if (msd == 0x4):
            # 4xkk - SNE Vx, byte. Skip next instruction if Vx != kk (increase PC by 2)
            if (self.v[x] != kk):
                self.pc += 2

        if (msd == 0x5):
            # 5xy0 - SE Vx, Vy. Skip next instruction if Vx == Vy (increase PC by 2)
            if (self.v[x] == self.v[y]):
                self.pc += 2

        if (msd == 0x6):
            # 6xkk - LD Vx, byte. Set Vx = kk
            self.v[x] = kk

        if (msd == 0x7):
            # 7xkk - ADD vx, byte. Set Vx = Vx + kk
            self.v[x] = self.v[x] + kk

        if (msd == 0x8):
            if (lsd == 0x0):
                # 8xy0 - LD Vx, Vy. Set Vx = Vy
                self.v[x] = self.v[y]

            if (lsd == 0x1):
                # 8xy1 - OR Vx, Vy. Set Vx = Vx OR Vy
                self.v[x] = self.v[x] | self.v[y]

            if (lsd == 0x2):
                # 8xy2 - AND Vx, Vy. Set Vx = Vx AND Vy
                self.v[x] = self.v[x] & self.v[y]

            if (lsd == 0x3):
                # 8xy3 - XOR Vx, Vy. Set Vx = Vx XOR Vy
                self.v[x] = self.v[x] ^ self.v[y]

            if (lsd == 0x4):
                # 8xy4 - ADD Vx, Vy. Set Vx = Vx + Vy, set Vf = carry
                val = self.v[x] + self.v[y]

                if (val > 0xFFFF):
                    val = val - 0xFF
                    self.v[0xF] = 0x1
                
                self.v[x] = val

            if (lsd == 0x5):
                # 8xy5 - SUB Vx, Vy. Set Vx = Vx - Vy, set Vf = NOT borrow
                val = self.v[x] - self.v[y]
                self.v[0xF] = 0x1

                if (val < 0x0):
                    val = val + 0xFF
                    self.v[0xF] = 0x0

                self.v[x] = val

            if (lsd == 0x6):
                # 8xy6 - SHR Vx {, Vy}. Set Vx = Vx SHR 1. If lsb of Vx is 1, then Vf = 1, else Vf = 0. Then Vx = Vx \ 2
                self.v[0xF] = self.v[x] & 0x1
                self.v[x] = self.v[x] > 1

            if (lsd == 0x7):
                # 8xy7 - SUBN Vx, Vy. Set Vx = Vy - Vx, set Vf = NOT borrow
                val = self.v[y] - self.v[x]
                self.v[0xF] = 0x1

                if (val < 0x0):
                    val = val + 0xFF
                    self.v[0xF] = 0x0

                self.v[x] = val

            if (lsd == 0xE):
                # 8xyE - SHL Vx {, Vy}. Set Vx = Vx SHL 1. If msb of Vx is 1, then Vf = 1, else 0. Then Vx = Vx * 2
                self.v[0xF] = self.v[x] & 0x80
                self.v[x] = (self.v[x] < 1) & 0xFF

        if (msd == 0x9):
            # 9xy0 - SNE Vx, Vy. Skip next instruction if Vx != Vy (increase PC by 2)
            if (self.v[x] != self.v[y]):
                self.pc += 2

        if (msd == 0xA):
            # Annn - Ld I, addr. Set IR = nnn
            self.ir = nnn

        if (msd == 0xB):
            # Bnnn - Jp V0, addr. Set PC = V0 + nnn
            self.pc = self.v[0x0] + nnn

        if (msd == 0xC):
            # Cxkk - RND Vx, byte. Set Vx = random byte [0, 255] AND kk
            self.v[x] = random.randint(0, 255) & kk

        if (msd == 0xD):
            # Dxyn - DRW Vx, Vy, nibble. Display n-byte sprite starting at mem location IR at (Vx, Vy), set Vf = collision
            pass

        if (msd == 0xE):
            if (lsd == 0xE):
                # Ex9E - SKP Vx. If key pressed on keyboard corresponds with value in Vx, increment PC by 2
                if (self.keyPressed == self.v[x]):
                    self.pc += 2

            if (lsd == 0x1):
                # ExA1 - SKNP Vx. If key not pressed on keyboard corresponds to value in Vx, increment PC by 2
                if (self.keyPressed != self.v[x]):
                    self.pc += 2

        if (msd == 0xF):
            if (y == 0x0):
                if (lsd == 0x7):
                    # Fx07 LD Vx, DT. Set Vx = delay timer value
                    self.v[x] = self.delayTimer

                if (lsd == 0xA):
                    # Fx0A - LD Vx, key. Store value of key press in Vx. All exeution is stopped until key is pressed.
                    key = -1
                    while (key == -1):
                        key = self.getKeyPress()
                    
                    self.v[x] = key

            if (y == 0x1):
                if (lsd == 0x5):
                    # Fx15 - LD DT, Vx. Set delay timer = Vx
                    self.delayTimer = self.v[x]

                if (lsd == 0x8):
                    # Fx18 - LD ST, Vx. Set sound timer = Vx
                    self.soundTimer = self.v[x]

                if (lsd == 0xE):
                    # Fx1E - Add I, Vx. Set IR = IR + Vx
                    self.ir = self.ir + self.v[x]

            if (y == 0x2):
                # Fx29 - LD F, Vx. Set IR = location of spite for digit Vx
                pass

            if (y == 0x3):
                # Fx33 - LD B, Vx. Store BCD represention of Vx in mem location IR, IR+1, and I+2
                num = self.v[x]
                hundredsDigit = num // 100
                num = num % 100
                tensDigit = num // 10
                num = num % 10
                onesDigit = num

                self.memory[ir] = format(hundredsDigit, 'x')
                self.memory[ir + 1] = format(tensDigit, 'x')
                self.memory[ir + 2] = format(onesDigit, 'x')

            if (y == 0x5):
                # Fx55 - LD [I], Vx. Store registers V0 to Vx in mem location starting at IR
                for i in range(x + 1):
                    memory[ir + i] = self.v[i]

            if (y == 0x6):
                # Fx65 - LD Vx, [I]. Read registers V0 to Vx from mem location starting at IR
                for i in range(x + 1):
                    self.v[i] = memory[ir + i]

    def execute(self):
        # Look up in dictionary
        # Might not need this function because execution is handled in decode func
        pass

    def updateTimers(self):
        # update timer stuff here
        pass
        
    def runOneCycle(self):
        fetch()
        decode()
        updateTimers()