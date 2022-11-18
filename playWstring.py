A=["this", "is", "africa", "africa", "africa", "africa", "africa", "africa", "africa", "africa", "africa"]
print (A)
print(A.count("africa"))


def removeWater(A):
    for i in range(A.count("africa")):
        A.remove("africa")
        print(A)


removeWater(A)