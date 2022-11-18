A=makePicture(pickAFile())
B=makePicture(pickAFile())

count=0
def quantificatori(A,B):
  allPx=getPixels(A)
  for i in range (0,len(getPixels(A))):
    px=allPx[i]
    currentLum= getRed(px)+getBlue(px)+getGreen(px)
    if not findLum(currentLum,B):
      return false
      
  return true
    
def findLum(inputLum,pict):
  allPx=getPixels(pict)
  for i in range (0,len(getPixels(pict))):
    px=allPx[i]
    currentLum= getRed(px)+getBlue(px)+getGreen(px)
    if inputLum==currentLum:
      return true
  return false

 
 
    