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

#print (ricorsione("fwhohv208ì93gh29'8hqnqo29g8f8209gh9o2983h298hr"))

# data una satringa s e un caratta ci restituire una nuova stringa aventi tutti i caratteri della stringa
# precedete trannle occorrenze di c

def delcar(s,c):
    #@param s: string
    #@param c: string
    assert len(c)==1
    if not s :
        return ""

    elif s[0]==c:
        return delcar(s[1:],c)

    else:
        return s[0]+ delcar(s[1:],c)

#print(delcar("osso","o"))

#stringa al contrario

def reversestr(s):
    if not s:
        return ""
    return reversestr(s[1:])+s[0]
print(reversestr("hello"))

#Write a function that takes in a base and an exp and recursively computes baseexp. You are not allowed to
#use the ** operator!

def potenza(b,e):
    if e==0:
        return 1
    elif e==1: return b
    else: return b*potenza(b,e-1)
#print(potenza(2,2))

#scrivere un afunzione ricorsiva che data una lista di strighe restituisce true se la media delle lunghezze delle stringhe
# presenti nella list al pari, false altrimenti

def medStr(l,c,sum):
    if not l:
        return (sum/c)%2==0
    return medStr(l[1:],c+1,sum+len(l[0]))

##print(medStr(["aa","bb"],0,0))

#################################
#scrivere una funzione ricorsiva che data una lista di stringhe restituisce il numero di stringhe nella lista che hanno il primo carattere uguale all'ultimo


def Prob17(l):
    #@param l:list
    if not l :
        return 0
    elif l[0][0]==l[0][-1]:
        return 1 + Prob17(l[1:])
    else:
        return Prob17(l[1:])

print(Prob17(["assa","osso","fwheipiewphfwihf","aaaaaaaaaaas"]))