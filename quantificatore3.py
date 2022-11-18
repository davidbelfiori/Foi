A=makePicture(pickAFile())

def quta3(A,k):
  
 #@param A: picture
 #@param k: int 
  for y in range (0,getHeight(A)):
    rigaRed=0
    for x in range (0,getWidth(A)):
      px=getPixel(A,x,y)
      pxRed=getRed(px)
      rigaRed+=pxRed
   
    if rigaRed==k:
      return true
    else :
     return false 
     break 
   
  
      
     
    
quta3(A,51177) 