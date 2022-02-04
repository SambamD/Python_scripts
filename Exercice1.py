# 1 Python script to check if a given number is a power of another one
from re import S
import sys
import math

given = sys.argv[1]
basee = sys.argv[2]

def isPowerOf():
    nmber = str(math.log(eval(given),eval(basee)))
    u,v = nmber.split(".")
    if v=='0':
        print("Yes !")
    else:
        print("No !")

isPowerOf()


## A simpler way
def is_Power(x, y):
   while (x%y == 0):
       x = x / y
   return x == 1