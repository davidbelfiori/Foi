#########################################################################
#Scrivere una funzione ricorsiva che calcoli la somma dei numeri da 1 a n.

def sum_recursive(n):
    if n == 1: # caso base
        return 1
    else:
        return n + sum_recursive(n-1) # chiamata ricorsiva


######################################################################
#Problema1. Scrivere una funzione ricorsiva che, data una lista di numeri interi (positivi o negativi), 
# restituisce come risultato la somma dei valori pari contenuti nella lista.Se la lista non contiene valori pari,
# la funzione restituisce 0

def listapari(l):
    if not l:
        return 0
    elif l[0]%2==0: return l[0]+ listapari(l[1:])
    else: return listapari(l[1:])

print(listapari([1,2,3,4,5,6,7,8]))

####################################################################
#Problema1. Scrivere una funzione ricorsiva che, data una lista L di stringhe, restituisce come risultato una stringa formata
# dalla concatenazione di tutte le stringhe in L aventi lunghezza dispari.Se la lista non contiene stringhe di lunghezza dispari,
# la funzione restituisce la stringa vuota.

def listadispari(l):
    if not l:
        return ""
    
    elif len(l[0])%2==1:
        return l[0]+ listadispari(l[1:])
    
    else: 
        return listadispari(l[1:])
    
print(listadispari(["asd","asdf","qwertyuio","rvehOàreqp","wperjgwpfjorepòfjoepòrjofpweojf"]))

#############################################################################
#Problema1. Scrivere una funzione ricorsiva che, data una lista di numeri interi (positivi o negativi), restituisce come 
# risultato il valore vero se la somma dei numeri contenuti nella lista è un valori pari, falso altrimenti.Se la lista è vuota,
# la funzione restituisce il valore vero

def sommalista(l,sum):
    if len(l)==0:
        return True
    if len(l)==1: 
        return (sum %2==0)
    else: 
        return sommalista(l[1:],l[0]+l[1])

print(sommalista([1,2,3,4,5,6],0))