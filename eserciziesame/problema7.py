#7. Si definisca una classe che ha come attributo una tupla di N interi aventi valore iniziale 0, 
# con N definito al momento della creazione di un oggetto della classe.
# Inoltre, la classe dispone di un metodo per visualizzare tutta la tupla, 
# e di un metodo (avente parametri ke i) che modifical'attributo tupla rimpiazzandolo con una nuova tupla dove il valore kè 
# stato sommato all'elemento in posizione idella vecchia tupla. Definire poi una classe derivata dalla prima, 
# dove il valore iniziale da assegnare a tutti gli elementi della tupla (uguale per tutti) 
# può essere specificato al momento della creazione di un oggetto della classe, tramite un opportuno
# parametro del costruttore. Fornire, inoltre, alcuni frammenti di codice Python che esemplificano 
# l'uso delle classi (creazione di oggetti delle due classi, uso dei metodi).
class tupla:
    def __init__(self,n):
        self.item=(0,)*n
    
    def visualizza(self):
        print(self.item) 
    
    def modifica(self,k,i):
        #non ho capito il testo 
        return 