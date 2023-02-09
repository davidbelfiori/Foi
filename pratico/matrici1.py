def modMatrix(matrix,a):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==a:
                matrix[i][j]="*"
    return matrix

#print(modMatrix([[1,2,3],[4,5,6],[7,8,9]],5))

def maxMatrix(matrix):
    max=matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]>max:
                max=matrix[i][j]
    return max
#print(maxMatrix([[1,2,3],[4,5,6],[7,8,9]]))
#Data una matrice contenente valori numerici è un intero k, la funzione Pone a
#zero ogni elemento che è multiplo di K

def zeroMatrix(mat,k):
    for i in range(0,len(mat)):
        for j in range (0,len(mat[0])):
            if mat[i][j]%k==0:
                mat[i][j]=0
    return mat
print(zeroMatrix([[1,2,3],[4,5,6],[7,8,9]],2))
