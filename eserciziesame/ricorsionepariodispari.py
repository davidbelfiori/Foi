#Scrivere una funzione ricorsiva che, data una lista di numeri interi (positivi o negativi), 
# restituisce come risultato il valore vero se la somma dei numeri contenuti nella lista è un valori pari, 
# falso altrimenti. Se la lista è vuota, la funzione restituisce il valore vero.

def ricorsione(l):
    if l==[]:
        return True
    elif len(l)==1:
        if l[0]%2==0:
            return True
        return False
    else:
        l[1]+=l[0]
        return ricorsione (l[1:])

numbers = [2, 4, 6, -3, 5]
# print(ricorsione(numbers))



def findx(l,x):
    if len(x) != 1:
        return False
    if len(l) == 0:
        return False
    elif x in l[0]:
         return True
    else:
        return findx(l[1:],x)
    
print(findx(["aa","ee","aoio","tumadre","ncsp"],"n"))
