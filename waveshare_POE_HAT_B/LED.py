import os
from PIL import Image , ImageDraw , ImageFont
from .SSD1306 import SSD1306

dir_path = os.path.dirname(os.path.abspath(__file__))

class LED:

    show = SSD1306()
    font_13 = ImageFont.truetype(dir_path+'/Courier_New.ttf',13)
    font_12 = ImageFont.truetype(dir_path+'/Courier_New.ttf',12)

    def __init__(self):
        self.show.Init()
        self.image1 = Image.new('1', (self.show.width, self.show.height), "WHITE")
        self.draw = ImageDraw.Draw(self.image1)
    
    def display(self, hostname, temp, FAN_MODE):
        # show.Init()
        # show.ClearBlack()
        
        self.image1 = Image.new('1', (self.show.width, self.show.height), "WHITE")
        self.draw = ImageDraw.Draw(self.image1)  
        self.draw.text((0,1), 'H:'+str(hostname), font = self.font_13, fill = 0)
        self.draw.text((0,15), 'Temp:'+ str(((int)(temp*10))/10.0), font = self.font_13, fill = 0)
        
        if FAN_MODE:
            self.draw.text((77,16), 'FAN:ON', font = self.font_12, fill = 0)
            self.FAN_ON()
        else:
            self.draw.text((77,16), 'FAN:OFF', font = self.font_12, fill = 0)
            self.FAN_OFF()
        
        self.show.ShowImage(self.show.getbuffer(self.image1))

    def ClearBlack(self):
        self.show.Init()
        self.show.ClearBlack()

    def string(self, string:str):
        self.image1 = Image.new('1', (self.show.width, self.show.height), "WHITE")
        self.draw = ImageDraw.Draw(self.image1)  
        self.draw.text((0,1), string, font = self.font_13, fill = 0)
        self.show.ShowImage(self.show.getbuffer(self.image1))
