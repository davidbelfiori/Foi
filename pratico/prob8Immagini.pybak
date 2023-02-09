
A=makeEmptyPicture(10,10,black)

def avgLumTot(A):
   allPx=getPixels(A)
   avgLum=0
   for i in range(0,len(allPx)):
     px=allPx[i]
     avgLum+=(getRed(px)+getBlue(px)+getGreen(px))/3
   return avgLum/len(allPx)

avgLumTot=avgLumTot(A)

def lum(A):
  avgCol=[]
  for i in range(0,getWidth(A)):
    avgLum=0
    for j in range(0,getHeight(A)):
      px=getPixel(A,i,j)
      avgLum+=(getRed(px)+getBlue(px)+getGreen(px))/3
    avgCol.append(avgLum)
  
  for k in range(0,len(avgCol)):
    if avgCol[k]!=avgLumTot:
      return False
  return True
  
 