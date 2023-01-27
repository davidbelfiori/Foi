#Scrivi una classe "Cerchio" che abbia come attributo il raggio e un metodo "calcola_area()" che restituisca l'area
# del cerchio (π * raggio^)

class cerchio:
    def __init__(self,r):
        self.raggio=r

    def calcolaArea(self):
        return 3.14*(self.raggio**2)


c=cerchio(5)
print(c.calcolaArea())

