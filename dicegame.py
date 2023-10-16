# Erstelle ein Würfelspiel!
# Du spielst gegen den Computer. Wenn das Spiel startet (mit einem kleinen Menü),hat der Spieler 6 Würfe.
# Er spielt dabei gegen den Computer. Wenn die Augensumme höher ist als jene des Computers hat der Spieler gewonnen,
# ansonsten der Computer.
import random

print("Würfelspiel")
print("Du spielst gegen den Computer. Wenn das Spiel startet, hast du 6 Würfe.")
print("Wenn die Augensumme höher ist als jene des Computers hast du gewonnen, ansonsten der Computer.")
print("Um zu würfeln drück Enter.")

while True:
    playerSum = 0
    compSum = 0
    for x in range(6):
        input()
        rand = random
        player = rand.randrange(6)
        comp = rand.randrange(6)
        print("Du hast eine " + str(player) + " gewürfelt.")
        print("Der Computer hat eine " + str(comp) + " gewürfelt.")
        playerSum += player
        compSum += comp
    if playerSum > compSum:
        print("Du hast " + str(playerSum) + ":" + str(compSum) + " gewonnen")
    elif playerSum < compSum:
        print("Der Computer hat " + str(playerSum) + ":" + str(compSum) + " gewonnen")
    else:
        print("Es ist unentschieden ausgefallen" + str(playerSum) + ":" + str(compSum))
