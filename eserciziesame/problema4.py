#Problema 5.
# Si definisca una classe PoligonoRegolare.
# Ogni oggetto della classe ha come attributi il numero di lati e la lunghezza di un lato,
# e come operazioni due metodi che restituiscono, rispettivamente, la lunghezza del lato e il perimetro del poligono.
# Si definisca inoltre una classe Qadrato, derivata dalla classe PoligonoRegolare,
# che ha un metodo aggiuntivo che restituisce l'area del quadrato.
# Dare la definizione completa delle due classi in Python, che include la definizione dei rispettivi costruttori 
# e dei metodi indicati. Fornire, inoltre, alcuniframmenti di codice Python che esemplificano
# l'uso delle classi (creazione di oggetti delle due classi, uso dei metodi).

class poligonoRegolare:
    def __init__(self,nlati,lenlato):
        self.nlati=nlati
        self.lenlato=lenlato
    
    def returnlen(self):
        return self.lenlato
    
    def perimetro(self):
        return self.lenlato*self.nlati

class quadrato(poligonoRegolare):
   
   def area(self):
        if self.nlati==4:
            return self.lenlato*self.lenlato
        else:
            return False

        
p=poligonoRegolare(nlati=4,lenlato=2)
q=quadrato(nlati=5,lenlato=4)


print(p.perimetro())
print(q.area())        
    