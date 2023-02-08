#data una matrice quadrata M , la funzione modifica M sostituendo con a tutti i valori sulla diagonale e sulla
# antidiagonale di M


def matrix(nR,nC):
    mat = []
    for i in range(nR):
        mat.append([0]*nC)
    return mat


def diagonale(mat,a):

    assert len(mat[0])==len(mat)

    for i in range(0,len(mat[0])):
        mat[i][i]=a

    return mat


def antiDiagonale(mat,a):

    assert len(mat[0])==len(mat)

    for i in range(0,len(mat[0])):

        mat[i][(len(mat[0])-1)-i]=a
    return mat

mat=matrix(3,3)
print(diagonale(mat,2))