#Scrivi una classe "Rettangolo" che abbia come attributi base e altezza. La classe deve avere un metodo "calcola_area()" che
# restituisca l'area del rettangolo (base * altezza), un metodo "calcola_perimetro()" che restituisca il perimetro del
# rettangolo (2 * (base + altezza)) e un metodo "verifica_quadrato()" che restituisca True se il rettangolo è un quadrato,
# False altrimenti.

class rettangolo:
    def __init__(self,base,altezza):
        self.base=base
        self.altezza=altezza

    def calcolaArea(self):
        return self.base*self.altezza

    def calcolaPerimetro(self):
        return 2*(self.base+self.altezza)

    def verificaQuadrato(self):
        if self.base==self.altezza:
            return True
        else:
            return False