#Problema1. Scrivere una funzione ricorsiva che, data una lista L di stringhe, 
# restituisce come risultato una stringa formata dalla concatenazione di tutte le stringhe in L aventi lunghezza dispari.
# Se la lista non contiene stringhe di lunghezza dispari, la funzione restituisce la stringa vuota.

def ricorsione(l,s):
    if len(l)==0:
        if s=="":
            return False
        else:
            return s
    else:
        if len(l[0])%2==0:
           return ricorsione(l[1:],s+l[0])
        else:
            return ricorsione(l[1:],s)
        
        
print(ricorsione(["ejwb","weuihp","ewruoò","wiohegweifphg"],""))