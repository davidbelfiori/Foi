# le matrici devono essere ben formate, tutte le righe della matrice devono avere stessa lunghezza
# il numero di elementi delle righe della matrice A deve essere uguale al numero di elementi nelle colonne di B
M3 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]


m1 = [[8, 14, -6],
      [12,7,4],
      [-11,3,21]]

m2 = [[3, 16, -6],
           [9,7,-4]]

def lenrighe(m):
    lenriga = len(m[0])
    for i in range(0, len(m)):
        if len(m[i]) != lenriga:
            return False
    return True


def moltiplicazione(m1, m2):
    if lenrighe(m1) and lenrighe(m2) == True:
        if len(m1[0]) == len(m2):
            for i in range(len(m1)):
                for k in range(len(m2)):
                    M3[i][k] = m1[i][k] * m2[i][k]
            return M3
        else:
            return  False
    else:
        return False

print(moltiplicazione(m1,m2))