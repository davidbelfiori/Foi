pict=makeEmptyPicture(100,100,red)

def verificaQuadrata():
  
  if (getWidth(pict)==getHeight(pict)):
   
    return   true 
    
    
def diagonale(pict,S,C):
  count=0
  if  (verificaQuadrata()==true ):
    for x in range (0,getWidth(pict)):
       px= getPixel(pict,x,x)
       colorPx=getColor(px)
       if (colorPx==C):
         count+=1
         
  return count > S
  
print diagonale(pict,99,red)
 
          
       
