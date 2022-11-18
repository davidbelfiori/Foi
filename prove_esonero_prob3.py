#pict=makePicture(pickAFile())
color=makeColor(200,99,101)
pict=makeEmptyPicture(100,100,color)
def problema(pict):
  count = 0
  allpx1=getPixels(pict)
  for x in range(0,len(allpx1)):
      px = allpx1[x]
      redPx=getRed(px)
      allpx=getPixels(pict)
      for z in range(0,len(getPixels(pict))):
        px2=allpx[z]
        gbPx=getBlue(px2)+getGreen(px2)
        if redPx!=gbPx and x==z:
          return False
          break 
        else: 
          return True , px ,px2 , x , z
           
        
        
 
  
 