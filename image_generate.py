from random import randint

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

ln=1

for i in range(0, ln):
    #img=Image.new("RGB", (700,450),(randint(0, 255),randint(0, 255),randint(0, 255)))
    img=Image.new("RGB",(562,390), (102,51,0))
    draw = ImageDraw.Draw(img)
    #draw.text((0, 0),"This is a test",(255,255,0))
    draw = ImageDraw.Draw(img)
    img.save(r'G:\My Drive\Installation\centos9\bg_images\\'+str(10)+".jpg", "JPEG")