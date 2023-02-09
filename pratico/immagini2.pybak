color=makeColor(200,100,100)
color2=makeColor(200,101,100)
m1=makeEmptyPicture(20,20,color)
m2=makePicture(pickAFile())
def verifica(A):
  for y in range(0,getHeight(A)):
    if riga(A,y)==true:
      return True
    
  return False
 
px11=getPixel(m1,1,4)
setColor(px11,black)
 
def riga(A,y):
  for i in range(0,getWidth(A)-1):
    px= getPixel(A,i,y)
    px2=getPixel(A,i+1,y)
    if getColor(px)!=getColor(px2):
      return false
  
  return true
  
