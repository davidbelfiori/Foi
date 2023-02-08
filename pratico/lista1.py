def ricorsione(l,a):
    if not l:
        return l
    elif l[0]%a!=0:
        return [l[0]]+ricorsione(l[1:],a)
    else:
        return ricorsione(l[1:],a)

print(ricorsione([1,2,3,4,5,6,7,8,9,10],2))