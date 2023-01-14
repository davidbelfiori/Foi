#Scrivere una funzione ricorsiva che data un stringa s restituisca la stringa ottenuta da s eliminando le vocali.
# Ad esempio l’invocazione eliminaVocali(‘pippo’) deve restituire la stringa ‘ppp’.

def ricorsione(s):
    l= 'aeiouAEIOU'
    if len(s)==0: 
        return s
    elif s[0] in l: return ricorsione(s[1:])
    
    return s[0] + ricorsione(s[1:])
    
print(ricorsione("pippo"))