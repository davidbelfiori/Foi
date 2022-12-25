def divisibile3(n):


    if n == 0:
        print("divisibile per 3")
    if (n == 3) or (n == 6) or (n == 9):
        print("divisibile per 3")
    else:
        lun = str(n)
        val = 0
        for i in range(0, len(str(n))):
            val = val + int(lun[i])
        divisibile3(val)


divisibile3(122)


