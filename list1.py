#Definire una funzione inserisci(L, n1, n2) : data una lista di interi L e due interi n1 e n2,
#la funzione restituisce una nuova lista ottenuta da L (senza modificare L) dove il valore n2 viene
#inserito subito dopo ogni occorrenza del valore n1.Esempio: inserisci ([3, 12, 4, 3, 10, 3], 3, 0)
#produce come risultato la lista [3, 0, 12, 4, 3, 0, 10, 3, 0]
mylist = [3, 12, 4, 3, 10, 3]


def ins(mylist, num1, num2):
    # @param mylist: list
    # @param num1:int
    # @param num2: int 
    s = []
    for i in range(0, len(mylist)):
        if mylist[i] == num1:
            s.append(mylist[i])
            s.append(num2)
        else:

             s.append(mylist[i])



    return s


print(ins(mylist, 3, 0))
