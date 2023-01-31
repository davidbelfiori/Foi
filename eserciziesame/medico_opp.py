class medico:
    def __init__(self, nome , specializzazione="non specificato"):
        self.nome=nome
        self.specializzazione=specializzazione
        self.colleghi=[]

    def getName(self):
        return self.nome

    def getSpecializzazione(self):
        return self.specializzazione

    def  getColleghi(self):
        return self.colleghi

    def addColleghi(self,medico):
        self.colleghi.append(medico.nome)

m1=medico("mario","cardiologo")
m2=medico("luca","cardiologo")
m3=medico("giovanni")
m4=medico("giuseppe","cardiologo")
m5=medico("antonio","cardiologo")
m6=medico("marco","cardiologo")
m7=medico("giacomo","cardiologo")

m1.addColleghi(m2)
m1.addColleghi(m3)
m1.addColleghi(m4)
m1.addColleghi(m5)
m1.addColleghi(m6)

print(m3.getName())

print(m1.getColleghi())
