from PIL import Image
from mp4toimages import splitvideotoframes
import os
currentframe = "frame0.jpg"
splitvideotoframes('movie.mp4')
count = 0
while True:
    try:
        im = Image.open(currentframe)
    except:
        print("DONE")
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
    os.remove(currentframe)
    currentframe  = "frame%d.jpg" % count
    print(Averagedrgb, currentframe, count)


#print(list(pixels[int(halfofimage)])+1)