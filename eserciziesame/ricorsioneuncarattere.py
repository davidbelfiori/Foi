#Si definisca una funzione ricorsiva che, data una lista di stringhe e una stringa x di un carattere,
#restituisce true se almeno una di queste stringhe contieneil carattere specificato da x, e false altrimenti.

def findx(x, l):
    if len(l) == 0:
        return False
    if x in l[0]:
        return True
    else:
        return findx(x, l[1:])

print(findx("x","wfnàekwfnikfpòwnx"))