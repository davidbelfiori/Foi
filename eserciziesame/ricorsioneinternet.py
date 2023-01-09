#Scrivere una funzione ricorsiva booleana che, data una stringa s, una stringa c di lunghezza 1, e un intero n,
# restituisce il valore vero se c è presente ALMENO n volte nella stringa s, falso altrimenti.

def ricorsione(s,c,n):
    if  len(s)==0 or len(c)>1:
        return False
    elif n==0: return True
    elif s[0]==c: return ricorsione(s[1:],c,n-1)
    else: return ricorsione(s[1:],c,n)
    
print(ricorsione("asdfghjkaaa","a",3))