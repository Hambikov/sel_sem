from PIL import Image
im = Image.open('img.ppm')
pixels = im.load() # create the pixel map

def redOrBlack (im):
    newimdata = []
    redcolor = (255,0,0)
    blackcolor = (0,0,0)
    for color in im.getdata():
        newimdata.append((color[0],0,0))
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim
redOrBlack(im).save('P5.ppm')
