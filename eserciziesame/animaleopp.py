#Crea una classe chiamata "Animale" che abbia attributi come nome, specie e età. 
# Includi anche metodi per emettere suoni diversi a seconda della specie dell'animale.

class animale:
    def __init__(self,nome,specie,eta):
        self.nome=nome
        self.specie=specie
        self.eta=eta


    def getnome(self):
        return self.nome

    def getSpecie(self):
        return self.specie

    def getEta(self):
        return self.eta

    def getSuono(self):
        if self.specie=="cane":
            return "bau"
        elif self.specie=="gatto": return "miaooooooooooooooooooooooo"
        elif self.specie=="topo": return  "forza lazieeeeeeeeeeeeeeeeeeeeee"
        else: return "non ce sta"

an=animale("gerry","topo",11)

print(an.getSuono())