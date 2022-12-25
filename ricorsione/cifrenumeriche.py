def cifrenumeriche(s,n,listnum):
    #@param s: string

    if len(s)==0:
        print("numero  di cifre", n ,"lista delle cifre numeriche",listnum)
    else:

        if s[0].isdigit():
            listnum.append(s[0])
            cifrenumeriche(s[1:],n+1,listnum)
        else:
            cifrenumeriche(s[1:], n , listnum)
cifrenumeriche('h9u8j91',0,[])