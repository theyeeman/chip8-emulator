"""Screen class to handle initialization, drawing, and updating. Top left of
screen is (x=0, y=0)
"""

from pygame import Color, display, draw

_pixelOff = Color(0, 0, 0, 255)
_pixelOn = Color(255, 255, 255, 255)

class Chip8Screen:
    def __init__(self, scale=10):
        """Initialize the screen object variables. The CHIP8 uses a 64x32 pixel 
        screen. A custom screen scale can passed to this function to suit any 
        size screen.
        """
        self.width = 64 * scale
        self.height = 32 * scale
        self.scale = scale
        self.pixelMap = []

    def initDisplay(self):
        """Initiazlizes the screen in pygame with the screen object variables.
        """
        display.init()
        self.surface = display.set_mode([self.width, self.height])
        self.clearScreen()
        self.update()

    def clearScreen(self):
        """Set all pixels on screen to off."""
        self.surface.fill(_pixelOff)

    def setPixel(self, x, y):
        """Set a pixel in the buffer to be on at a specific x, y location. Need
        to call update() to load the buffer onto the screen.
        """
        x_pos = x * self.scale
        y_pos = y * self.scale

        draw.rect(self.surface, _pixelOn, 
                (x_pos, y_pos, self.scale, self.scale))

    def resetPixel(self, x, y):
        """Set a pixel in the buffer to be off at a specific x, y location. Need
        to call update() to laod the buffer onto the screen.
        """
        x_pos = x * self.scale
        y_pos = y * self.scale

        draw.rect(self.surface, _pixelOff, 
                (x_pos, y_pos, self.scale, self.scale))

    def getPixel(self, x, y):
        """Return true if pixel at position (x, y) is on."""
        x_pos = x * self.scale
        y_pos = y * self.scale

        pixelState = self.surface.get_at((x_pos, y_pos))

        if (pixelState == _pixelOff):
            return False
        else:
            return True
    
    def getPixelMap(self):
        """Store the current screen of pixels in a 2D array. Used for save 
        states.
        """
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
        """Draws a byte onto the screen. Since a byte is 8-bits in length, this
        function will draw an 8 pixel wide line starting at location x, y. The
        CHIP8 uses an XOR to draw, so a pixel that is already on will be turned
        off when it is drawn on again. Returns whether a pixel collision 
        happened.
        """
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
        """Get the width of the screen."""
        return self.width

    def getHeight(self):
        """Get the height of the screen."""
        return self.height

    def getScale(self):
        """Get the scale of the screen."""
        return self.scale

    def update(self):
        """Update the screen with the buffer."""
        display.flip()

    def destroy(self):
        """Destroy the current screen."""
        display.quit()