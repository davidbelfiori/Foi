def ndigitalpha(s,c,n):
    #@param s: string
    # @param
    # @param c:int
    # @param n:int
    if len(s)==0:
        if c==n:
            print("true")
        else:
            print("false")
    else:
        if s[0].isdigit():
            ndigitalpha(s[1:],c,n+1)
        else:
            ndigitalpha(s[1:], c+1, n)

ndigitalpha("a1b2c3",0,0)