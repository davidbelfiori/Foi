pic=makeEmptyPicture(500,400)
k=50
def lineaverticale(x):        
  for y in range (0,50):
    pix=getPixel(pic,x,y*z)
    setColor(pix,black)
    
for z in range (1,8):
  for x in range (0,50):
    pix=getPixel(pic,x+50*z,50*z)
    lineaverticale(x)
    setColor(pix,black)
    



show (pic)