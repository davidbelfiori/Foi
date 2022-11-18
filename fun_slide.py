pict=makePicture(pickAFile())

#riduce del 50% il rosso in pgni pixel
def reduceRed(pict,x):
#@param pict: Picture
#@Param x: Int
  for p in getPixels(pict):
    originalRed=getRed(p)
    setRed(p,originalRed*x) 

#riduce del 50% il verde in pgni pixel   
def reduceGreen(pict,x):
#@param pict: Picture
#@Param x: Int
  for p in getPixels(pict):
    originalGreen=getGreen(p)
    setGreen(p,originalGreen*x)

#riduce del 50% il blu in pgni pixel
def reduceBlue(pict,x):
#@param pict: Picture
#@Param x: Int
  for p in getPixels(pict):
    originalBlue=getBlue(p)
    setBlue(p,originalBlue*x)

#creare un negativo riducendo le componeti RGB
def negative(pict) :
# @param pict: Picture
  for p in getPixels(pict):
    red=getRed(p)
    green=getGreen(p)
    blue=getBlue(p)
    negColor=makeColor( 255-red, 255-green, 255-blue)
    setColor(p, negColor)
   

#creare un bianco e nero   
def greyScale(pict):
  for p in getPixels(pict):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    greyTone = makeColor( intensity, intensity, intensity)
    setColor(p, greyTone)

#togliere la componente rgb blue    
def clearBlue(pict):
  for p in getPixels(pict):
    setBlue(p,0)
  
#togliere la componente rgb rossa 
def clearRed(pict):
  for p in getPixels(pict):
    setRed(p,0)
  
#togliere la componente rgb verde 
def clearGreen(pict): 
  for p in getPixels(pict):
    setGreen(p,0)   
  
#effetto tramonto 
def makeSunset(pict):
  for p in getPixels(pict):
    value=getBlue(p)
    setBlue(p,value*0.7)
    value=getGreen(p)
    setGreen(p,value(*0.7))
  
 
def decreaseRed2(pict,x):
# @parampict: Picture
  for x in range(0, getWidth(pict)):
    for y in range(0, getHeight(pict)):
      px= getPixel(pict,x,y)
      originalRed= getRed(px)
      setRed(px, originalRed*x)
  
  
  
def privacy2(pict, xmin, xmax, ymin, ymax) :
# @param pict: Picture
# @param xmin, xmax, ymin, ymax: int
  for x in range(xmin, xmax) :
    for y in range(ymin, ymax) :
      pix = getPixel(pict, x, y)
      setColor(pix, black)
  

def mirrorVertical(source):
# @paramsource: Picture;
  width = getWidth(source)
  mirrorPoint= width / 2
  for y in range(0, getHeight(source)):
    for x in range(0, mirrorPoint):
       leftPixel= getPixel(source, x, y)
       rightPixel= getPixel(source, width -x-1, y)
       color = getColor(leftPixel)
       setColor(rightPixel, color)

def mirrorHorizontal(source):
# @paramsource: Picture;
  height = getHeight(source)
  mirrorPoint= height/ 2
  for x in range(0, getWidth(source)):
    for y in range(0, mirrorPoint):
      topPixel= getPixel(source, x, y)
      bottomPixel= getPixel(source, x, height -y-1)
      color = getColor(topPixel)
      setColor(bottomPixel, color)

def mirrorBotTop(source):
# @paramsource: Picture;
  height = getHeight(source)
  mirrorPoint= height / 2
  for x in range(0, getWidth(source)):
    for y in range(0, mirrorPoint):
      topPixel= getPixel(source, x, y)
      bottomPixel= getPixel(source, x, height -y-1)
      color = getColor(bottomPixel)
      setColor(topPixel, color)  
 
                                                                            
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
      setColor(pix,red)
      
      
def diagonalePiccola2(pic):
# @param pic: picture immagine creata 
  for x in range (getWidth(pic),getWidth(pic)/2,-1):
      for y in range(0, getHeight(pic)/2):
        pix=getPixel(pic,(getWidth(pic)-y)-1,(getHeight(pic)/2)+y)
        setColor(pix,green)
    
                                                                                                                                                                                                                      