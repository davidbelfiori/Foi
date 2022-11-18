#pict= makePicture(pickAFile())
pic=makeEmptyPicture(500,500)


for y in range (min(150,getHeight(pic)),250):
  
  for x in range (min(150,getWidth(pic)),350):
    px=getPixel(pic,x,y)
    setColor(px,black)
    
show(pic) 