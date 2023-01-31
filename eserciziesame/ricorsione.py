# Scrivere una funzione ricorsiva che restituisca il massimo elemento in una lista di numeri.

def ricorsione(l, m):
    if len(l) == 0:
        return m
    elif l[0] > m:
        m = l[0]
        return ricorsione(l[1:], m)
    else:
        return ricorsione(l[1:], m)


# print(ricorsione([1,2,3,4,5,6],0))


def somma(n):
    if int(n) < 10:
        return n
    else:
        n = str(n)
        return int(n[0]) + int(somma(n[1:]))


# print(somma(122))


# Scrivere una classe chiamata "Automobile" che rappresenti un'auto con i seguenti attributi:
# marca, modello, anno e velocità.

# Includere metodi nella classe per:

# accelerare l'auto di una certa quantità (ad esempio, 10 mph)
# frenare l'auto di una certa quantità (ad esempio, 5 mph)
# stampare i dettagli dell'auto (marca, modello, anno, velocità attuale)

# Creare un'istanza della classe "Automobile" e utilizzare i metodi per modificare la velocità e stampare
# i dettagli dell'auto.


class Automobile:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.velocita = 0

    def accellera(self, acc):
        self.velocita += acc

    def frena(self, fren):
        self.velocita -= fren

    def getAuto(self):
        return self.marca, self.modello, self.anno, self.velocita


# Problema 1. Scrivere una funzione ricorsiva che, data una stringa s, restituisce una nuova stringa ottenuta
# eliminando da s tutti i caratteri alfabetici (si ricordi a tale scopo il metodo isalpha() del tipo di dato str).

def ricorsione(s):
    if len(s) == 0:
        return ""
    else:
        if s[0].isalpha():
            return ricorsione(s[1:])
        return s[0] + ricorsione(s[1:])


# print (ricorsione("fwhohv208ì93gh29'8hqnqo29g8f8209gh9o2983h298hr"))

# data una satringa s e un caratta ci restituire una nuova stringa aventi tutti i caratteri della stringa
# precedete trannle occorrenze di c

def delcar(s, c):
    # @param s: string
    # @param c: string
    assert len(c) == 1
    if not s:
        return ""

    elif s[0] == c:
        return delcar(s[1:], c)

    else:
        return s[0] + delcar(s[1:], c)


# print(delcar("osso","o"))

# stringa al contrario

def reversestr(s):
    if not s:
        return ""
    return reversestr(s[1:]) + s[0]


print(reversestr("hello"))


# Write a function that takes in a base and an exp and recursively computes baseexp. You are not allowed to
# use the ** operator!

def potenza(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    else:
        return b * potenza(b, e - 1)


# print(potenza(2,2))

# scrivere un afunzione ricorsiva che data una lista di strighe restituisce true se la media delle lunghezze delle stringhe
# presenti nella list al pari, false altrimenti

def medStr(l, c, sum):
    if not l:
        return (sum / c) % 2 == 0
    return medStr(l[1:], c + 1, sum + len(l[0]))


##print(medStr(["aa","bb"],0,0))

#################################
# scrivere una funzione ricorsiva che data una lista di stringhe restituisce il numero di stringhe nella lista che hanno il primo carattere uguale all'ultimo


def Prob17(l):
    # @param l:list
    if not l:
        return 0
    elif l[0][0] == l[0][-1]:
        return 1 + Prob17(l[1:])
    else:
        return Prob17(l[1:])


# print(Prob17(["assa","osso","fwheipiewphfwihf","aaaaaaaaaaas"]))

# Scrivere una funzione ricorsiva che, data una stringa s, restituisce come risultato una stringa ottenuta elimanando
# da s tutti i caratteri ripetuti consecutivamente, tranne il primo (Es.: se s = ‘aaabbcccc’ la funzione deve restituire
# ‘abc’; se s = ‘ababcc’ la funzione deve restituire ‘ababc’.

def delateDuplicate(s):
    if len(s) <= 1:
        return s
    elif s[0] == s[1]:
        return delateDuplicate(s[1:])
    else:
        return s[0] + delateDuplicate(s[1:])

# print(delateDuplicate("asssaaass"))

# Scrivere una funzione ricorsiva che data un stringa s restituisca la stringa ottenuta da s eliminando le vocali.
# Ad esempio l’invocazione eliminaVocali(‘pippo’) deve restituire la stringa ‘ppp’.

def delvocali(s):
    if not s:
        return ""
    elif s[0] in "aeiou":
        return delvocali(s[1:])
    else:
        return s[0] + delvocali(s[1:])


#Scrivete una funzione ricorsiva che accetti un elenco di numeri e restituisca True se l'elenco è ordinato e False in caso contrario.

def isSorted(l):

    if len(l) <= 1:
        return True
    elif l[0] > l[1]:
        return False
    else:
        return isSorted(l[1:])

#print(isSorted([1,3,4,5,2]))


#Scrivere una funzione ricorsiva che data una lista di stringhe l e un carattere c restituisce il numero di stringhe che
# contengono almeno 2 volte il carattere c

def occorrenze2(l,c):
    if not l:
        return  0
    elif l[0].count(c)>=2:
        return  1+ occorrenze2(l[1:],c)
    else: return occorrenze2(l[1:],c)

#print(occorrenze2(["assaa","osso","fwheipiewphfwihf","aaaaaaaaaaas"],"a"))

def ovenlist(l):
    if not l:
        return []
    elif l[0]%2==1: return [l[0]] + ovenlist(l[1:])
    else: return ovenlist(l[1:])

#print(ovenlist([1,2,3,4,5,6,7,8,3,4,5,6,7,8,8,765]))

#Problema 1. Scrivere una funzione ricorsiva che, data una stringa s, restituisce come risultato una stringa formata da tutti
# i caratteri di s separati tra loro da uno spazio bianco.Esempio: data la stringa "abcd", la funzione deve restituire
# la stringa "a b c d"

def space(s):
    if not s:
        return ""
    elif len(s)==1:
        return s[0]
    else:
        return s[0]+" "+space(s[1:])

#print(space("abcd"))

#Scrivere una funzione ricorsiva che, data una lista L di stringhe, restituisce come risultato una stringa formata dalla
# concatenazione di tutte le stringhe in L aventi lunghezza dispari.Se la lista non contiene stringhe di lunghezza dispari,
# la funzione restituisce la stringa vuota.

def oddlen(l):
    if not l:
        return ""
    elif len(l[0])%2==1:
        return l[0]+oddlen(l[1:])
    else:
        return  oddlen(l[1:])

#print(oddlen(["assaa","osso","fwheipiewphfwihf","aaaaaaaaaaas","aaaaa"]))

#data un astringa s di qualunque lunghezza scrivere una funzione ricorsiva che:
# 1) restituisce il numero di cifre numeriche in s

def numRep(s):
    if not s:
        return 0
    elif s[0].isnumeric():
        return 1+ numRep(s[1:])
    else:
        return  numRep(s[1:])

#print(numRep("assaa1osso2fwheipiewphfwihf3aaaaaaaaaaas4aaaaa"))

#data un astringa s di qualunque lunghezza scrivere una funzione ricorsiva che: restituisce in una lista le cifre presenti nella stringa s

def numRepList(s):
    if not s:
        return []
    elif s[0].isnumeric():
        return [s[0]] + numRepList(s[1:])
    else:
        return  numRepList(s[1:])

#print(numRepList("assaa1osso2fwheipiewphfwihf3aaaaaaaaaaas4aaaaa"))


def numupper(s):
    if not s:
        return 0
    elif s[0].isupper():
        return 1+ numupper(s[1:])
    else:
        return  numupper(s[1:])

#scrivi un programma ceh converta da decimale a binario

def dec2bin(n):
    if n==0:
        return ""
    else:
        return dec2bin(n//2) + str(n%2)


#Data una lista di interi formata da un qualunque numero di elementi e un
#intero n, la funzione restituisce una nuova lista formata da solo elementi di
#L che non sono immediatamente seguiti dal valore n

def grassi1(l,n):
    if not l:
        return []
    elif len(l)==1: return  l
    elif l[1]!=n:
        return [l[0]]+grassi1(l[1:],n)
    else:
        return  grassi1(l[1:], n)



L=[5,10,5,10,105]
n=5
def seleziona(L,n):
    if len(L)==0:
        return []
    elif len(L)==1:
        return L
    else:
        if L[1]==n:
            return seleziona(L[1:],n)
        if not L[1]==n:
            return [L[0]] + seleziona(L[1:],n)
#print(grassi1(L,n))

#Scrivere una funzione ricorsiva che, data una stringa s, restituisce vero se la stringa
#contiene la stessa quantità di cifre numeriche e caratteri alfabetici, falso
#altrimenti.

def alphadigit(s,d,a):
    if not s:
        return a==d
    elif s[0].isdigit():
        return  alphadigit(s[1:],d+1,a)
    else:
        return  alphadigit(s[1:],d,a+1)


#print(alphadigit("ass111aa11",0,0))

#Scrivere una funzione ricorsiva che, data una stringa s, restituisce come
#risultato una stringa ottenuta elimanando da s tutti i caratteri ripetuti
#consecutivamente, tranne il primo (Es.: se s = "aaabbcccc" la funzione deve
#restituire "abc"; se s = "ababcc" la funzione deve restituire "ababc".

def elimina(s):
    if not s:
        return ""
    elif len(s)==1:
        return s
    elif s[0]==s[1]:
        return elimina(s[1:])
    else:
        return s[0]+elimina(s[1:])
#print(elimina("abcabcabc"))

#Scrivere una funzione ricorsiva che, data una lista L di stringhe,
#restituisce come risultato una stringa formata dalla concatenazione di tutte
#le stringhe in L aventi lunghezza dispari. Se la lista non contiene stringhe
#di lunghezza dispari, la funzione restituisce la stringa vuota.

def listaoven(l):
    if not l:
        return ""
    elif len(l[0])%2==1:
        return l[0]+listaoven(l[1:])
    else:
        return listaoven(l[1:])
#print(listaoven(["assaaaa","osso","fwheipiewphfwihf","aaaaaaaaaaas","aaaaaa"]))

#Scrivere una funzione ricorsiva che, data una stringa s, restituisce vero se
#la stringa contiene solo coppie consecutive formate da una cifra numerica e
#un carattere alfabetico; falso altrimenti.

def alfadigitCons(s):
    if not s:
        return True
    elif len(s)==1:
        return  False
    elif s[0].isdigit() and s[1].isalpha():
        return alfadigitCons(s[2:])
    else:
        return False
#print(alfadigitCons("1a2b3c1"))

#Scrivere una funzione ricorsiva booleana che, data una stringa s, una stringa
#c di lunghezza 1, e un intero n, restituisce il valore vero se c è presente
#ALMENO n volte nella stringa s, falso altrimenti.

def almenoN(s,n,c):
    assert len(c)==1
    if not s :
        return  n==0
    elif n==0:
        return True
    elif s[0]==c:
        return almenoN(s[1:],n-1,c)
    return  almenoN(s[1:],n,c)

#print(almenoN("ciaoccc",2,"c"))
#Scrivere una funzione ricorsiva che data un stringa s restituisca la stringa
#ottenuta da s eliminando i numeri.ù

def delNum(s):
    if not s:
        return ""
    elif s[0].isdigit():
        return delNum(s[1:])
    else:
        return s[0]+delNum(s[1:])
#print(delNum("ass243453digfrewy"))

#scrivere una ricorsiva che data una stringa s mette maiuscolo o minuscolo le
#lettere

def upperLower(s):
    if len(s)==0:
        return ""
    elif s[0]==s[0].upper():
        return s[0].lower()+upperLower(s[1:])
    elif s[0]==s[0].lower():
        return  s[0].upper() + upperLower(s[1:])
    else: return s[0]+upperLower(s[1:])
print(upperLower("ciAo-"))