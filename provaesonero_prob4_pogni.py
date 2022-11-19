color=makeColor(200,100,100)
color2=makeColor(200,101,100)
A=makeEmptyPicture(30,30,color)

def foo(A):
  allpx=getPixels(A)
  for i in range (0,len(allpx)):  
    px= allpx[i]
    redPx=getRed(px)
    if b(redPx,i)==false:
        return False
  return True
  
def b(redPx,i):
  allPx2=getPixels(A)
  for j in range (0,len(allPx2)):
    px2=allPx2[j]
    if (i!=j):
      if (redPx==getGreen(px2)+getBlue(px2)):
        return true 
      else: 
        return false 
print (foo(A))