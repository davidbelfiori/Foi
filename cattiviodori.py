a=makePicture(pickAFile())

def lum(px):
  return (getRed(px)+getGreen(px)+getBlue(px)/3)

def mediariga(a):
  
  ListAvg=[]
  for  y in range (0 , getHeight(a)):
    avgLum=0
    avgLum1=0
    for x in range(0,getWidth(a)):
    
      px=getPixel(a,x,y)
      avgLum1+=lum(px)
      avgLum=avgLum1/getWidth(a)
    ListAvg.append(avgLum)
  
  return ListAvg
 
def righeUguali():
  count=0
  ListAvg2=mediariga(a)
  for i in range (0,500):
    if ListAvg2.count(i)>1:
      count+=1
  return count
  
