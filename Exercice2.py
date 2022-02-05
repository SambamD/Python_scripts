# Find missing numbers from a list
myTmpList = []
def findMissing(myList):
    for j in range(min(myList),max(myList)+1):
        if (j not in myList):
            print(j)

findMissing([1,2,3,4,6,7,10])