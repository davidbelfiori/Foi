m = [[1, 2, 3, 10], [3, 5, 7, 2], [4, 9, 2, 5]]


def croce(m, i, j):
    #@param m : list
    # @param i: int riga
    # @param j : int colonna
    nord = True
    sud = True
    est = True
    ovest = True

    if i > 0:
        nord = (m[i][j] > m[i - 1][j])
    if i < len(m) - 1:
        sud = (m[i][j] > m[i + 1][j])
    if j > 0:
        ovest = (m[i][j] > m[i][j - 1])
    if j < len(m[0]) - 1:
        est = (m[i][j] > m[i][j + 1])
    return (nord and sud and ovest and est)


print(croce(m, 1, 2))
