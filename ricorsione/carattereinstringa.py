#Scrivere una funzione ricorsiva che, data una stringa s, una stringa c di lunghezza 1, e un intero n,
#restituisce il valore vero se c è presente ALMENO n volte nella stringa s, falso altrimenti.

def stringa(s, c, n,g):
    # @param s : string
    # @param c: string len=1
    # @param n: int

    if g>=n:
        print("true")

    else:
        if len(s)>0:
             if s[0]==c:
                 stringa(s[1:],c,n,g+1)
             else:
                 stringa(s[1:], c, n, g)
        else:
            print("false")
stringa("ciccio","c",4,0)