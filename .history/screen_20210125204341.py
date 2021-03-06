# Screen class to handle initialization, drawing, and updating.
from pygame import Color, display, draw

pixelOff = Color(0, 0, 0, 255)
pixelOn = Color(255, 255, 255, 255)

# (top, left) is (0, 0)

class chip8_Screen:
    def __init__(self, scale):
        self.width = 64 * scale
        self.height = 32 * scale
        self.scale = scale
        self.pixelMap = []

    def initDisplay(self):
        display.init()
        self.surface = display.set_mode([self.width, self.height])
        self.clearScreen()
        self.update()

    def clearScreen(self):
        # Set all pixels on screen to off
        self.surface.fill(pixelOff)

    def setPixel(self, x, y):
        # Set a pixel in the buffer to be on at a specific x, y location. Need to call update()
        # to actually make it show on screen
        x_pos = x * self.scale
        y_pos = y * self.scale

        draw.rect(self.surface, pixelOn, (x_pos, y_pos, self.scale, self.scale))

    def resetPixel(self, x, y):
        # Set a pixel in the buffer to be off at a specific x, y location. Need to call update()
        # to actually make it show on screen
        x_pos = x * self.scale
        y_pos = y * self.scale

        draw.rect(self.surface, pixelOff, (x_pos, y_pos, self.scale, self.scale))

    def getPixel(self, x, y):
        # Return true if pixel at position (x, y) is on
        x_pos = x * self.scale
        y_pos = y * self.scale

        pixelState = self.surface.get_at((x_pos, y_pos))

        if (pixelState == pixelOff):
            return False
        else:
            return True
    
    def getPixelMap(self):
        # Store the current screen of pixels in a 2D array. Used for save states
        self.pixelMap.clear()
        tempMap = []

        for y in range(32):
            for x in range(64):
                if (self.getPixel(x, y)):
                    tempMap.append(1)
                else:
                    tempMap.append(0)
            self.pixelMap.append(tempMap.copy())
            tempMap.clear()

    def byteToPixel(self, x, y, byte):
        # Byte is 8-bits. Return whether pixel was turned off
        setVF = False

        for i in range(7, -1, -1):
            mask = 1
            if (byte & (mask << i) != 0):
                # Pixel at (x, y) commanded on
                if (not self.getPixel((x + 7 - i) % 64, y % 32)):
                    # Pixel is off, so turn on this pixel
                    self.setPixel((x + 7 - i) % 64, y % 32)
                else:
                    # Pixel is already on, so turn this pixel off and set v[0xF]
                    self.resetPixel((x + 7 - i) % 64, y % 32)
                    setVF = True
        
        return setVF

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getScale(self):
        return self.scale

    def update(self):
        # Update the screen with the buffer.
        display.flip()

    def destroy(self):
        # Destroy the current screen
        display.quit()