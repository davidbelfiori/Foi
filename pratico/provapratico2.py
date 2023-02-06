color=makeColor(200,100,100)
color2=makeColor(200,101,100)
P=makeEmptyPicture(30,30,color)

def esame(P,a,b):
  
  for i in range(0,getHeight(P)):
    px1=getPixel(P,a,i)
    px2=getPixel(P,b,i)
    colPx1=getColor(px1)
    colPx2=getColor(px2)
    if colPx1!=colPx2:
      return False
  return True
 
def prova(A):
  for i in range(0,getHeight(A)):
    px=getPixel(A,10,i)
    setColor(px,blue)