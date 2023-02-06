color=makeColor(200,100,100)
color2=makeColor(200,101,100)
m1=makeEmptyPicture(20,20,color)
m2=makeEmptyPicture(20,20,color)
def contenuto(m1,m2):
  allpx=getPixels(m1)
  for i in range(0,len(getPixels(m1))):
    pxM1=allpx[i]
    colM1=getColor(pxM1)
    if cercaM2(colM1,m2):
      return True
  return False
 
def cercaM2(colM1,m2):
  allpx=getPixels(m2)
  for j in range(0,len(getPixels(m2))):
    pxM2=allpx[j]
    colM2=getColor(pxM2)
    if colM2==colM1:
       return true
  return false
    
  