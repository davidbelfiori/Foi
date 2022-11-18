#Problema 9
#Scrivere una funzione Python che, data un'immagine A e un intero c, 
#restituisce la somma delle componenti Green dei colori presenti nella colonna numero c.

pict=makePicture(pickAFile())

def problema9(pict,c):
 #@parma pict: picture
 #@param c: int //colonna 
  greenPx=0
  for y in range (0, getHeight(pict)):
    px=getPixel(pict,c,y)
    greenPx+=getGreen(px)
  
  return greenPx