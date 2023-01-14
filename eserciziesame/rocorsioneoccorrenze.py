#Assegnata una stringa S ed un carattere c, scrivere una funzione ricorsiva che calcoli le occorrenze di c in S

def ricorsione(s,c,sum ):
    if len(s)==0:
        return sum 
    elif s[0]==c : return ricorsione(s[1:],c,sum+1)
    return ricorsione(s[1:],c,sum)

print (ricorsione("aaadpjaaapj","a",0))