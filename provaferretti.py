def foo(s):
    n=""
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if j>i:
                if (s[i]==s[j] and s[i]!="" ):
                    n+=s.replace(s[j],"*")

            
    return n
    

print(foo("ciao come stai"))