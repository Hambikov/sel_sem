import cv2
image=cv2.imread("img.ppm",cv2.IMREAD_GRAYSCALE)

from PIL import Image
im = Image.open('gray.ppm')
pixels = im.load()
print(pixels)
coords = []
for i in range(len(image)-90):
  for j in range(len(image[0])-80):
      top = image[i+30][j+80] - image[i][j+80] - image[i+30][j] + image[i][j]
      mid = image[i+60][j+80] - image[i+30][j+80] - image[i+60][j] + image[i+30][j]
      bottom = image[i+90][j+80] - image[i+60][j+80] - image[i+90][j] + image[i+60][j]
      left = image[i+60][j+30] - image[i+30][j+30] - image[i+60][j] + image[i+30][j]
      center = image[i+60][j+50] - image[i+30][j+50] - image[i+60][j+30] + image[i+30][j+30]
      right = image[i+60][j+80] - image[i+30][j+80] - image[i+60][j+50] + image[i+30][j+50]
      top_left = image[i+30][j+40] - image[i][j+40] - image[i+30][j+10] + image[i][j+10]
      top_center = image[i+30][j+50] - image[i][j+50] - image[i+30][j+30] + image[i][j+30]
      top_right = image[i+30][j+70] - image[i][j+70] - image[i+30][j+50] + image[i][j+50]
      if(top > 1.2*mid) and (bottom > 1.2*mid) and (center > 0.9*left) and (center > 0.9*right) and (top_center > center) and (top_left > center) and (top_right > center):
          coords.append((i,j))
def del_replay(cor):
  max_dif = 20
  l = []
  c = 0
  while c!=len(cor)-1:
    mh = cor[c][0]
    mw = cor[c][1]
    c += 1
    l = []
    for i in enumerate(cor):
      if (abs(i[1][0]-mh)+abs(i[1][1]-mw) <= max_dif):
        l.append(cor[i[0]])
    cor = l
  return cor
coords = del_replay(coords)
print(coords)
def pict(i,j):
  newimdata = []
  for x in range(i.size[1]):
    for y in range(im.size[0]):
      for color in i.getdata():
        if j[1]<=x<=j[1]+80 and j[0]<=y<=j[0]+90:
            newimdata.append((0,0,0))
  newim = Image.new(im.mode,im.size)
  newim.putdata(newimdata)
  return newim
for i in coords:
  im = pict(im,i)
im.save('4ungle.ppm')
