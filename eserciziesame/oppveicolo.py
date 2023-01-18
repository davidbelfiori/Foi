#Problema 2. Si definisca una classe Veicolo. Ogni oggetto della classe ha come attributi la sua targa e il suo anno di costruzione, 
# e come operazioni due metodi che restituiscono, rispettivamente, targa e anno di costruzione del veicolo. Si definisca inoltre
# una classe Automobile, derivata dalla classe Veicolo, che ha due attributi aggiuntivi indicanti la cilindrata e il massimo numero
# di persone trasportabili, e i corrispondent metodi per conoscere il valore di questi attributi. Dare la definizione completa delle
# due classi in Python, che include la definizione dei rispettivi costruttori e dei metodi indicati. Fornire, inoltre, alcuni frammenti 
# di codice Python che esemplificano l'uso delle classi (creazione di oggetti delle due classi, uso del valore dei loro attributi).

class Veiclolo:
    
    def __init__(self,targa,acost):
        self.targa=targa
        self.acost=acost
    
    def get_targaa(self):
        return self.targa
    
    def get_acostruzione(self):
        return self.acost

class Automobile(Veiclolo):
    
        def __init__(self, targa, acost,cilindrata,omologata):
             super().__init__(targa, acost)
             self.cilindrata=cilindrata
             self.omologata=omologata
             
        def cilindra (self):
            return self.cilindrata
        
        def nposti(self):
            return self.omologata

auto=Automobile("FG533LZ",2016,1000,4)
a=auto.get_acostruzione()
print(a)