#Scrivere una funzione ricorsiva che, dato una lista di interi l, restituisca una nuova lista di interi ottenuto 
# da l sostituendo ogni numero negativo con 0. Ad esempio l’invocazione azzeraNegativi({1,-2, 3, 4, -5}), 
# deve restituire l’array {1, 0, 3, 4, 0}.

def ricorsione(l): 
    if not l :
        return l
    elif l[0]<0: 
        l[0]=0 
        return [l[0]] + ricorsione(l[1:])
    return [l[0]] + ricorsione(l[1:])

print(ricorsione([1,-2, 3, 4, -5]))