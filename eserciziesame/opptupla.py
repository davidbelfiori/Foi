#Si definisca una classe che ha come attributo una tupla di N interi aventi valore iniziale 0, 
# con N definito al momento della creazione di un oggetto della classe. Inoltre, la classe dispone di un metodo per visualizzare
# tutta la tupla, e di un metodo (avente parametri ke i) che modifica l'attributo tupla rimpiazzandolo con una nuova tupla dove il 
# valore k è stato sommato all'elemento in posizione i della vecchia tupla. Definire poi una classe derivata dalla prima, dove il 
# valore iniziale da assegnare a tutti gli elementi della tupla (uguale per tutti) può essere specificato al momento della creazione
# di un oggetto della classe, tramite un opportuno parametro del costruttore. Fornire, inoltre, alcuni frammenti di codice Python che 
# esemplificano l'uso delle classi (creazione di oggetti delle due classi, uso dei metodi)

class tupla: 
    def __init__(self,n):
        self.n=n
        self.tl=(0,)*n

    def showtupla(self):
        return (self.tl)
            
    def replace(self ,k ,i):
        if i < len(self.tl)-1:
            ntl=self.tl[:i]+ self.tl[i]+k + self.tl[i+1:]
        else: 
            valtl=self.tl[i]
            ntl=self.tl[:i]+ (valtl+k, )
            

tk=tupla(4)
print (tk.showtupla())

tk.replace(7,3)
print (tk.showtupla())