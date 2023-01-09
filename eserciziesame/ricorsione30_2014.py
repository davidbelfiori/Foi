# Scrivere una funzione ricorsiva che, data una lista di numeri interi (positivi o negativi),
# restituisce come risultato il valore vero se la somma dei numeri contenuti nella lista è un valori pari, 
# falso altrimenti.Se la lista è vuota, la funzione restituisce il valore vero

def ricorsione(l):
    if not l :
        return False
    
    return (l[0] + ricorsione(l[1:]))%2==0 
    
print(ricorsione([1,2,3]))
    