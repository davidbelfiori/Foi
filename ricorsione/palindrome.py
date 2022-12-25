def palindrome(s):
    #@param s : string
    if len(s)== 0 or len(s)==1:
        print("palindroma")
    else:
        a=s[:1]
        b=s[len(s)-1:]
        if a==b:

            palindrome(s[1:len(s)-1])
        else:
            print("non palindroma")


palindrome("ossessox")