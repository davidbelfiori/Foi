## Crea una classe Prodotto che ha come parametri nome, tipologia, prezzo, numero prodotti disp. Crea dei metodi per aggiungere e
# vendere prodotti, un altro metodo per apllicare uno sconto al prodotto e getProdotto

class prodotto:
    def __init__(self,nome,tipologia):
        self.nome=nome
        self.tipologia=tipologia
        self.prezzo=0
        self.nprodotti=0

    def addprod(self,prezzo,qta):
        self.prezzo=prezzo
        self.nprodotti=qta

    def vendita(self,nome,qta):
        self.nprodotti-=qta

    def addsconto(self,sconto):
        self.prezzo-=sconto

    def getPRodotto(self):
        return self.nome,self.tipologia,self.prezzo,self.nprodotti

p=prodotto("pasta","alimentare")
p.addprod(1.5,100)
p.vendita("pasta",10)
p.addsconto(0.5)
print(p.getPRodotto())