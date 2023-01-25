#Scrivere una funzione ricorsiva che restituisca il massimo elemento in una lista di numeri.

def ricorsione(l,m):
    if len(l)==0:
        return m
    elif l[0]>m:
        m=l[0]
        return ricorsione(l[1:],m)
    else:
        return ricorsione(l[1:],m)

# print(ricorsione([1,2,3,4,5,6],0))


def somma(n):
    if int(n) < 10:
        return n
    else:
        n = str(n)
        return int(n[0]) + int(somma(n[1:]))
    

# print(somma(122))



# Scrivere una classe chiamata "Automobile" che rappresenti un'auto con i seguenti attributi: 
# marca, modello, anno e velocità.

# Includere metodi nella classe per:

# accelerare l'auto di una certa quantità (ad esempio, 10 mph)
# frenare l'auto di una certa quantità (ad esempio, 5 mph)
# stampare i dettagli dell'auto (marca, modello, anno, velocità attuale)

# Creare un'istanza della classe "Automobile" e utilizzare i metodi per modificare la velocità e stampare 
# i dettagli dell'auto.


class Automobile:
    def __init__(self,marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.velocita = 0
        
    def accellera(self, acc):
        self.velocita += acc
        
    def frena(self, fren):
        self.velocita -= fren
        
    def getAuto(self):
        return self.marca, self.modello, self.anno, self.velocita
        
#Problema 1. Scrivere una funzione ricorsiva che, data una stringa s, restituisce una nuova stringa ottenuta 
# eliminando da s tutti i caratteri alfabetici (si ricordi a tale scopo il metodo isalpha() del tipo di dato str).
    
def ricorsione (s):
    if len(s)==0:
        return ""
    else:
        if  s[0].isalpha():
            return  ricorsione(s[1:])
        return s[0]+ricorsione(s[1:])

print (ricorsione("fwhohv208ì93gh29'8hqnqo29g8f8209gh9o2983h298hr"))