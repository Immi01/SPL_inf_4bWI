import random
# Erstelle eine Zufallszahl zwischen 0 und 100 Random

rand = random
randomNumber = rand.randrange(100)

# Gib die Zufallszahl aus

print(randomNumber)

# Wenn die Zahl kleiner ist als 20 gib aus "Mini"

if(randomNumber < 20):
    print("Mini")

# Wenn die Zahl zw. 20 und 50 ist gib aus "Medium"

if(randomNumber > 20 and randomNumber < 50):
    print("Medium")

# Wenn die Zahl größer als 50 ist gib aus "Large"

if(randomNumber > 50):
    print("Large")
