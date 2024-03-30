import smbus

class FAN:

    def __init__(self,address = 0x20):
        self.i2c = smbus.SMBus(1)
        self.address = address
        # self.FAN_ON()
        # self.FAN_MODE = 0
        
    def FAN_ON(self):
        self.i2c.write_byte(self.address, 0xFE & self.i2c.read_byte(self.address))
        
    def FAN_OFF(self):
        self.i2c.write_byte(self.address, 0x01 | self.i2c.read_byte(self.address))
