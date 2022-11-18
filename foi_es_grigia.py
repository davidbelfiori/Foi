
file= pickAFile()
pic= makePicture(file)
col=red
w=50
def bandaDiag(pic,w,col):
 for h in range(0,min( getHeight(pic),getWidth(pic))):
   drawHorizontalLineGen(pic,h,h,w,col)

def drawHorizontalLineGen(pic,x,y,w,col):
  for c in range(x,min(x+w,getWidth(pic))):
    setColor(getPixel(pic,c,y),col)


bandaDiag(pic,w,col)
show(pic)