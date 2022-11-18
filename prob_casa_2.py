pic=makeEmptyPicture(500,500)

def diagonale1(pic):
# @param pic: picture immagine creata 
  for x in range (0,getWidth(pic)):
    for y in range (0,1):
      pix=getPixel(pic,x,x)
      setColor(pix,black)
    
    
def diagonale2(pic):
# @param pic: picture immagine creata 
  for x in range (getWidth(pic),0,-1):
       for y in range(0,1):
        pix=getPixel(pic,x-1,getWidth(pic)-x)
        setColor(pix,blue)
        

def diagonalePiccola(pic):
# @param pic: picture immagine creata 
  for x in range (0,getWidth(pic)/2):
      pix=getPixel(pic,x,(getHeight(pic)/2)+x)
      setColor(pix,black)
      
      
def diagonalePiccola2(pic):
# @param pic: picture immagine creata 
  for x in range (getWidth(pic),getWidth(pic)/2,-1):
      for y in range(0, getHeight(pic)/2):
        pix=getPixel(pic,(getWidth(pic)-y)-1,(getHeight(pic)/2)+y)
        setColor(pix,green)

def digonaleAltadx(pic):
  for x in range (0,getWidth(pic)/2):
      pix=getPixel(pic,x,(getWidth(pic)/2)-x)
      setColor(pix,red)
      
def diagonaleAltasx(pic):
  for x in range (0,getWidth(pic)/2):
    pix=getPixel(pic,(getWidth(pic)/2)+x,x)
    setColor(pix,red)

def rettacentrale (pic):
  for x in range(0,getWidth(pic)):
    pix=getPixel(pic,x,getWidth(pic)/2)
    setColor(pix,black)
     
diagonale1(pic)
diagonale2(pic)
diagonalePiccola(pic)
diagonalePiccola2(pic)
digonaleAltadx(pic)
diagonaleAltasx(pic)
rettacentrale(pic)
show(pic)