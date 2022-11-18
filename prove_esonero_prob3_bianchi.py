color=makeColor(200,99,101)
A = makeEmptyPicture(40, 40,color)

def foo(A):
# @param A: picture
  D = getPixels(A)
  for i in range(0, len(D)):
    compRed = getRed(D[i])
    if B(D, compRed,i):
      return True 
  return False
    
    
    

def B(pxs, compRed,num):
# @param D: sequence of pixel
# @param compRed: int
  for i in range(0, len(pxs)):
    if (getBlue(pxs[i]) + getGreen(pxs[i])) == compRed:
      return True 
  return False

print foo(A)