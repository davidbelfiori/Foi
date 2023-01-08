#Problema1. Scrivere una funzione ricorsiva che, data una lista di numeri interi (positivi o negativi),
# restituisce come risultato la somma dei valori pari contenuti nella lista.
# Se la lista non contiene valori pari, la funzione restituisce 0


def ricorsione (l,s):
  
  if len(l)!=0:
  
    if l[0]%2==0 and int(l[0])==l[0]:
        
        return ricorsione(l[1:],s+l[0])
    else:
        return ricorsione(l[1:],s)
        
  else:
       if s!=0:
           return s
       else:
           return False

print (ricorsione([1,2,3,4,5,6,7,8],0))
