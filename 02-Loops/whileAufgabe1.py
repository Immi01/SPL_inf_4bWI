# Erstelle ein Programm, dass Zufallszahlen zwischen 10 und 30 generiert.
# Das Programm soll die Zufallszahlen zusammenzählen.
# Sobald die Zahl 15 oder die Zahl 25 kommt,
# wird das Programm beendet und die Summe der vorherigen Zufallszahlen ausgegeben!
import random

rand = random
randNum = 0
sum = 0

while randNum != 15 and randNum != 25:
    sum += randNum
    randNum = rand.randrange(10, 30)

print(sum)
