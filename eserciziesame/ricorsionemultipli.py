#Si definisca una funzione ricorsiva che, data una lista L, un valore V e un intero k,
# restituisce true se il valore V è presente in tutte le posizioni della lista il cui indice è multiplo di k,
# e false altrimenti.

def ricorsione(l,v,k):
    if len(l)==0:
        return True
    elif len(l)<  k:
        return l[k]==v
    else:
        return ricorsione(l[1:],v,k*2)
    
print(ricorsione(["aa","aa","bb","aa","cc"],"aa",2))