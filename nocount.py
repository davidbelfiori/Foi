a = "pippo"
listA = ["pippo", "pluto", "paperino", "giovanni", "pippo"]


def nocount(listA, a):
    #@parmam listA:list
    #@param a:string
    count = 0
    for ele in listA:
        if a == ele:
            count += 1
    return count

