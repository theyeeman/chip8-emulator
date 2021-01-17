# Opcode information from http://devernay.free.fr/hacks/chip8/C8TECH10.HTM
from random import randint
import pygame
import winsound
from pygame.locals import (
    K_1,
    K_2,
    K_3,
    K_4,
    K_q,
    K_w,
    K_e,
    K_r,
    K_a,
    K_s,
    K_d,
    K_f,
    K_z,
    K_x,
    K_c,
    K_v,
    KEYDOWN,
    KEYUP
)

class chip8_Emulator:
    def __init__(self, screen):
        self.screen = screen
        self.pc = 0x200  # Program counter
        self.ir = 0  # Index Register
        self.v = [0] * 16  # CPU Registers
        self.op = 0x0  # Current Opcode
        self.sp = 0  # Stack pointer
        self.keyPressed = -1
        self.memory = [0] * 4096
        self.stack = [0] * 16
        self.delayTimer = 0
        self.soundTimer = 0
        self.running = True
        self.beepFreq = 2500
        self.beepDuration = 1000


        fontSet = {
            0 :[0xF0, 0x90, 0x90, 0x90, 0xF0],
            1 : [0x20, 0x60, 0x20, 0x20, 0x70],
            2 : [0xF0, 0x10, 0xF0, 0x80, 0xF0],
            3 : [0xF0, 0x10, 0xF0, 0x10, 0xF0],
            4 : [0x90, 0x90, 0xF0, 0x10, 0x10],
            5 : [0xF0, 0x80, 0xF0, 0x10, 0xF0],
            6 : [0xF0, 0x80, 0xF0, 0x90, 0xF0],
            7 : [0xF0, 0x10, 0x20, 0x40, 0x40],
            8 : [0xF0, 0x90, 0xF0, 0x90, 0xF0],
            9 : [0xF0, 0x90, 0xF0, 0x10, 0xF0],
            10 : [0xF0, 0x90, 0xF0, 0x90, 0x90],
            11 : [0xE0, 0x90, 0xE0, 0x90, 0xE0],
            12 : [0xF0, 0x80, 0x80, 0x80, 0xF0],
            13 : [0xE0, 0x90, 0x90, 0x90, 0xE0],
            14 : [0xF0, 0x80, 0xF0, 0x80, 0xF0],
            15 : [0xF0, 0x80, 0xF0, 0x80, 0x80]
            }

        # Load font set into memory
        i = 0
        for font in fontSet.values():
            for byte in font:
                self.memory[i] = byte
                i += 1

    def loadROM(self, file, offset):
        data = open(file, 'rb').read()
        for index, byte in enumerate(data):
            self.memory[index + offset] = byte

    def eventHandler(self):
        # Handles events for closing pygame window, keypresses, and sound timer beep
        self.keyPressed = -1

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False

            if (event.type == KEYDOWN):
                self.keyPressed = self.keyMap(event.key)

        if (self.soundTimer > 0):
            winsound.Beep(self.beepFreq, self.beepDuration)

    def keyMap(self, keys):
        # Converts valid key press into hex value. Invalid key press
        # is treated as no key pressed and has value -1
        if (keys == K_x):
            return 0x0
        elif (keys == K_1):
            return 0x1
        elif (keys == K_2):
            return 0x2
        elif (keys == K_3):
            return 0x3
        elif (keys == K_q):
            return 0x4
        elif (keys == K_w):
            return 0x5
        elif (keys == K_e):
            return 0x6
        elif (keys == K_a):
            return 0x7
        elif (keys == K_s):
            return 0x8
        elif (keys == K_d):
            return 0x9
        elif (keys == K_z):
            return 0xA
        elif (keys == K_c):
            return 0xB
        elif (keys == K_4):
            return 0xC
        elif (keys == K_r):
            return 0xD
        elif (keys == K_f):
            return 0xE
        elif (keys == K_v):
            return 0xF
        else:
            return -1

    def fetchOpcode(self):
        self.op = 0x0
        self.op = (self.memory[self.pc] << 8) | self.memory[self.pc + 1]
        self.pc += 2

    def executeOpcode(self):
        # Parsing opcode into format 0x[msd][x][y][lsd]
        msd = self.op >> 12
        x = (self.op & 0x0F00) >> 8
        y = (self.op & 0x00F0) >> 4
        lsd = self.op & 0x000F
        kk = self.op & 0x00FF
        nnn = self.op & 0x0FFF

        if (msd == 0):
            if (lsd == 0):
                # 00E0 - CLS. Clear display
                self.screen.clearScreen()

            else:
                # 00EE - RET. Return from subroutine. Set PC to top of stack, then decrement SP
                self.pc = self.stack.pop()
                self.sp -= 1

        if (msd == 0x1):
            # 1nnn - JP addr. Set PC to nnn
            self.pc = nnn

        if (msd == 0x2):
            # 2nnn - CALL addr. Increment SP, push current PC to stack, then set PC to nnn
            self.stack.append(self.pc)
            self.pc = nnn
            self.sp += 1

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
            self.v[x] += kk

            if (self.v[x] > 255):
                self.v[x] -= 256
                self.v[0xF] = 1

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
                self.v[x] += self.v[y]

                if (self.v[x] > 255):
                    self.v[x] -= 256
                    self.v[0xF] = 1

            if (lsd == 0x5):
                # 8xy5 - SUB Vx, Vy. Set Vx = Vx - Vy, set Vf = NOT borrow
                self.v[x] -= self.v[y]
                self.v[0xF] = 1

                if (self.v[x] < 0):
                    self.v[x] += 256
                    self.v[0xF] = 0

            if (lsd == 0x6):
                # 8xy6 - SHR Vx {, Vy}. Set Vx = Vx SHR 1. If lsb of Vx is 1, then Vf = 1, else Vf = 0. Then Vx = Vx \ 2
                self.v[0xF] = self.v[x] & 0x1
                self.v[x] = self.v[x] >> 1

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
                self.v[x] = (self.v[x] << 1) & 0xFF

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
            self.v[x] = randint(0, 255) & kk

        if (msd == 0xD):
            # Dxyn - DRW Vx, Vy, nibble. Display n-byte sprite starting at mem location IR at (Vx, Vy), set Vf = collision

            self.v[0xF] = 0
            pixelCollision = False

            for i in range(lsd):
                pixelCollision = self.screen.byteToPixel(self.v[x], self.v[y] + i, self.memory[self.ir + i])

            if (pixelCollision):
                self.v[0xF] = 1

            self.screen.update()

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
                    while (self.keyPressed == -1):
                        self.eventHandler()

                    self.v[x] = self.keyPressed

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
                    self.ir = self.v[x] * 5

            if (y == 0x3):
                # Fx33 - LD B, Vx. Store BCD represention of Vx in mem location IR, IR+1, and I+2
                num = self.v[x]
                hundredsDigit = num // 100
                num = num % 100
                tensDigit = num // 10
                num = num % 10
                onesDigit = num

                self.memory[self.ir] = hundredsDigit
                self.memory[self.ir + 1] = tensDigit
                self.memory[self.ir + 2] = onesDigit

            if (y == 0x5):
                # Fx55 - LD [I], Vx. Store registers V0 to Vx in mem location starting at IR
                for i in range(x + 1):
                    self.memory[self.ir + i] = self.v[i]

            if (y == 0x6):
                # Fx65 - LD Vx, [I]. Read registers V0 to Vx from mem location starting at IR
                for i in range(x + 1):
                    self.v[i] = self.memory[self.ir + i]
        
    def decrementTimers(self):
        self.delayTimer -= 1
        self.soundTimer -= 1
        
        if (self.delayTimer < 0):
            self.delayTimer = 0
        if (self.soundTimer < 0):
            self.soundTimer = 0

    def runOneCycle(self):
        self.eventHandler()
        self.fetchOpcode()
        self.executeOpcode()
        self.decrementTimers()