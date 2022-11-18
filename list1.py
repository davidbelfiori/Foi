mylist = [8, 0, 2, 1, 4, 8, 9]


def ins(mylist, num1, num2):
    # @param mylist: list
    # @param num1:int
    # @param num2: int 
    s = []
    for i in range(0, len(mylist)):
        s.append(mylist[i])
    s.append(num1)
    s.append(num2)
    return s


print(ins(mylist, 3, 0))
