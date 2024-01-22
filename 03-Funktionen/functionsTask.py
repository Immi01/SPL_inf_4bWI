# Erstelle eine Funktion die 2 Zahlen addiert
# Erstelle eine Funktion, die eine zufällige Zahl zwischen 100 und 200 zurückliefert
# Erstelle eine Funktion, die ein Wort aus einem String Array zurückliefert.
import random


def addfunction(num1, num2):
    added = num1 + num2
    return added


def randfunction():
    rnd = random.randrange(100, 200)
    return rnd


def rndWort(wordArray):
    rnd = random.randrange(len(wordArray))
    return wordArray[rnd]

num1 = 3
num2 = 8
print(addfunction(num1, num2))

print(randfunction())

words = ["Banane", "Apfel", "Auto"]
print(rndWort(words))
