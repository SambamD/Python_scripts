# Write a Python program to find x numbers from an array such that the sum of x numbers equal to y
from itertools import combinations
myArray = []
def findXnumbers(myArray,x,y):
    for i in combinations(myArray,x):
        if(sum(i)==y):
            print(i)

findXnumbers([-1,2,-4,5,-2,3,1],3,0)