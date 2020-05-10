from PIL import Image
from mp4toimages import splitvideotoframes
import os
currentframe = "frame0.jpg"
splitvideotoframes(input('Please write the file name e.g. "example.mp4"'))
count = 0
# fuck you dont read my code slut
while True:
    try:
        im = Image.open(currentframe)
    except:
        exit() 
    im = Image.open(currentframe)
    pixels = list(im.getdata())
    amountofpixels = len(pixels)
    width, height = im.size
    forloopspot = 0
    currentspot = 0
    totalr = 0
    totalb = 0
    totalg = 0
    currentframeint = 0

    for i in range(amountofpixels):
        currentpixellist = list(pixels[int(currentspot)])
        totalr += currentpixellist[0]
        totalb += currentpixellist[1]
        totalg += currentpixellist[2]
        currentspot += 1

    totalr = int(totalr/amountofpixels)
    totalb = int(totalb/amountofpixels)
    totalg = int(totalg/amountofpixels)

    Averagedrgb = (totalr, totalb, totalg)
    count += 1
    print(Averagedrgb, currentframe)
    os.remove(currentframe)
    currentframe  = "frame%d.jpg" % count
    

#print(list(pixels[int(halfofimage)])+1)