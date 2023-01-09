#Scrivere una funzione ricorsiva che, data una lista L di stringhe, restituisce come risultato una stringa formata 
# dalla concatenazione di tutte le stringhe in L aventi lunghezza dispari.Se la lista non contiene stringhe di lunghezza dispari,
# la funzione restituisce la stringa vuota.

def ricrosione(l):
    if not l :
        return ""
    if len(l[0])%2==1: 
        return l[0]+ricrosione(l[1:])
    return ricrosione(l[1:])

#print(ricrosione(["a", "abc", "def", "ghij"]))
#Problema1. Scrivere una funzione ricorsiva che, data una lista di numeri interi (positivi o negativi), restituisce come risultato
# la somma dei valori pari contenuti nella lista.Se la lista non contiene valori pari, la funzione restituisce 0.

def ricorsione2(l):
    if not l : 
        return 0
    if l[0]%2==0: 
        return l[0]+ricorsione2(l[1:])
    return ricorsione2(l[1:])

print(ricorsione2([1, 2, 3, 4, 5]))
print(ricorsione2([1, 3, 5, 7]))