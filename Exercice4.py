# Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit

def addDigits(n):
    som=0
    while(n >=10):
        som=0
        for index,valeur in enumerate(str(n)):
            valeur = int(valeur)
            som+=valeur
        n=int(som)
    print(som)


addDigits(10)