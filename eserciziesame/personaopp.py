#Problema 2.Si consideri una classe Persona che ha come attributi il nome, l'età, e gli amici della persona,
# rappresentati come una lista di oggetti di tipo Persona. La classe dispone di metodi per conoscere il nome della persona, 
# l'età della persona, e per aggiungere un nuovo amico all'insieme degli amici già presenti.Dare la definizione completa della classe,
# che include la definizione di un adeguato costruttore e dei tre metodi indicati. Fornire, inoltre, alcuni frammenti di codice Python 
# che esemplificano l'uso della classe (creazione di un oggetto "persona", stampa del suo nome e/o età, inserimento di un amico).

class persona: 
    def __init__(self,eta,nome):
        self.eta=eta
        self.nome=nome
        self.amici=[]
    
    def name(self):
        return self.nome
    
    def dob(self):
        return self.eta
    
    
    
    def addamici(self,amico):
        self.amici.append(amico)
        
#Problema 3. Data la classePersona definita nel problema precedente,  si consideri la classe derivata Insegnante, che possiede come
# attributi aggiuntivi la materiainsegnata e lo stipendio percepito, e come metodi aggiuntivi i metodi che consentono di conoscere il 
# nome della matera, lo stipendio dell'insegnante, e di modificare il nome della materia insegnata.Dare la definizione completa della
# classe derivata, che include la definizione di un adeguato costruttore e dei tre metodi indicati. Fornire, inoltre, alcuni frammenti 
# di codice Python che esemplificano l'uso della classe.

class insegnante(persona):
    def __init__(self,nome,eta,mat,sal):
        persona.__init__(nome,eta)
        self.mat=mat
        self.sal=sal
   
    def retmat(self):
        return self.mat
    
    def retsal(self):
        return self.sal
    
    def modMat(self,nMat):
        self.mat=nMat
        