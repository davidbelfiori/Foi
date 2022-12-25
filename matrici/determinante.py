def verifica2x2(m1):
    # @param m : matrix
    if len(m1) == 2:
        num = len(m1[0])
        for i in range(0, len(m1)):
            if num != len(m1[i]):
                return False
        return True


def deleteRowColum(m,riga,colonna):
    #@param m : matrix
    #@param riga: int
    #@param colonna: int
    newM=[]
    for i in range(0,len(m)):
        newR=[]
        for j in range (0,len(m[0])):
            if (i!=riga) and (j!=colonna):
                newR.append(m[i][j])

        if len(newR)!=0:
            newM.append(newR)
    return newM




def det22(m1):
    # @param m1 : matrix
    if verifica2x2(m1):
        det = (m1[0][0] * m1[1][1]) - (m1[0][1] * m1[1][0])
        return det
    else:
        return "matrice non conforme"


m1 = [[2, 2], [1, 3]]


def Determinant3(m):
    # @param m: Matrix
    # return Float
    assert len(m) == 3, "La matrice non ha 3 righe"
    for i in range(0, len(m)):
        assert len(m[i]) == 3, "La matrice non ha 3 colonne"

    det = 0
    for i in range(0, len(m)):
        if (m[0][i] != 0):
            newM = deleteRowColum(m, 0, i)
            det = det + m[0][i] * ((-1) ** (i)) * det22(newM)

    return det

print(Determinant3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))