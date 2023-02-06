class giocatore:
    def __init__(self,nickname):
        #@param nickname: str
        self.nickname=nickname
        self.punteggi=[]


    def addPunteggio(self,pto):
        #@param pto:
        self.punteggi.append(pto)
        return self.punteggi

    def getNickname(self):
        return self.nickname

    def getPunteggioMedio(self):
        avg=0
        for i in range(0,len(self.punteggi)):
            avg+=self.punteggi[i]
        return avg/len(self.punteggi)

class giocatorePuls(giocatore):
    def __init__(self,nickane,immagine):
        giocatore.__init__(self,nickane)
        self.immagine=immagine

    def getGiocatore(self):
        return self.nickname,self.immagine,self.getPunteggioMedio()


g1=giocatore("mario")
g1.addPunteggio(10)
g1.addPunteggio(20)
g1.addPunteggio(30)


g2=giocatorePuls("luca","immagine")
g2.addPunteggio(10)
g2.addPunteggio(20)

print(g1.getNickname())
print(g1.getPunteggioMedio())
print(g2.getGiocatore())
print(g2.getPunteggioMedio())

