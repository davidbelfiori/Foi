#Crea una classe chiamata "Libro" che abbia attributi come titolo, autore e numero di pagine. Includi anche
# metodi per ottenere informazioni sul libro e per impostare un segnalibro.

class libro:
    def __init__(self,autore,titolo,npagine):
        self.autore=autore
        self.titolo=titolo
        self.npagine=npagine
        self.segnalibro=0

    def getAutore(self):
        return self.autore

    def getTitolo(self):
        return self.titolo

    def getNpagine(self):
        return self.npagine

    def setSegnalibro(self,n):
        self.segnalibro=n

    def getSegnalibro(self):
        return  self.segnalibro