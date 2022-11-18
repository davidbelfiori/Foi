pict=makePicture(pickAFile())
minLum=255
for x in range(0,len(getPixels(pict))):
    px= getPixels(pict)
    cRed=getRed(px[x])
    cBlue=getBlue(px[x])
    cGreen=getGreen(px[x])
    lum=(cRed+cBlue+cGreen)/3
    if(lum<minLum):
      minLum=lum
print minLum

        

          
       
