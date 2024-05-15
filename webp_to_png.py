import os
from PIL import Image
from pathlib import Path

srcdir = r'C:\Users\srinivas\OneDrive\Desktop\temp2'
destdir = r'C:\Users\srinivas\OneDrive\Desktop\temp2'
destdir1 = r'C:\Users\srinivas\OneDrive\Desktop\temp2'
files = [ f for f in os.listdir(srcdir) if os.path.isfile(os.path.join(srcdir,f)) ]

#for i in files:
#    if i.endswith('.webp'):
#        im = Image.open(destdir+"\\"+str(i)).convert("RGB")
#        im.save(destdir+"\\"+str(i)+".png", "png")
#        os.remove(destdir+"\\"+str(i))

for i in files:
    if i.endswith('.jpg'):
        im = Image.open(srcdir+"\\"+str(i)).convert("RGB")
        im.save(destdir+"\\"+str(i)+".png", "png")
        #os.remove(destdir+"\\"+str(i))

#print(files)

#for i in files:
#        if i.endswith('.png.png'):
#            filename = Path(i).with_suffix('')
#            os.rename(destdir + "\\" + str(i), destdir + "\\" + str(filename))
#            print(str(filename))