pic=makeEmptyPicture(600,500)
def scale(pic,k,r,col):
  # @param pic: picture 
  # @param k : int punt di inzio della scala 
  # @param r: int lunghezza dei gradini 
  # @param col : instance colore 
  lastY=0
  lastX=0
  nextX=0
  nextY=0
  print type(col)
  h=(getWidth(pic)/r)+1
  print h
  for z in range (1,11):
    for x in range (0,r): #lunghezza della riga orizzontale 
      pix=getPixel(pic,min(getWidth(pic)-1,x+nextX),min(getHeight(pic)-1,nextY+k))
      
     # print "x+netxX:",x+nextX
      setColor(pix,col)
      lastX=x
    nextX=lastX*z
   # print "nextX:",nextX
    for y in range (0,r): #lunghezza della riga verticale 
      pix=getPixel(pic,min(getWidth(pic)-1,nextX),min(getHeight(pic)-1,nextY+y+k))
     # print "y+nety:",y+nextY
      setColor(pix,col)
      lastY=y
    nextY=lastY*z
   # print "NEXTy:",nextY 
      
scale(pic,20,70,blue)
show(pic)
