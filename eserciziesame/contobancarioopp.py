#Crea una classe chiamata "Conto Bancario" che abbia attributi come numero di conto, proprietario e saldo.
# Includi anche metodi per effettuare depositi, prelievi e visualizzare il saldo.

class conto:
    def __init__(self,nconto,proprietario,saldo):
        self.nconto=nconto
        self.proprietario=proprietario
        self.saldo=saldo

    def getConto(self):
        return "il numero del conto è: "+self.nconto + " il proprietario è: "+self.proprietario+ " il saldo è: "+str(self.saldo)

    def deposito(self,cash):
        if  cash>0:
            self.saldo+=cash
        else: print("operazione errata")

    def prelievo(self,n):
        if self.saldo>=n:
            self.saldo = self.saldo-n
            return self.saldo
        else: return "operazione errata"

    def getSaldo(self):
        return self.saldo