# Diese Aufgabe setzt sich aus allen gelernten Inhalten zusammen!
# Erstelle ein Programm, das einen Bankomaten simuliert. Folgende Möglichkeiten gibt es:
# 1. Einzahlen
# 2. Abheben
# 3. Kontostand
# 4. Beenden
import decimal

print("Bankomat")

balance = 0

while True:
    print("Geben Sie die Entsprechende Nummer für die Aktion die sie ausführen wollen ein:")
    print("1. Einzahlen")
    print("2. Abheben")
    print("3. Kontostand")
    print("4. Beenden")

    valErr = False
    choice = input()
    choice = int(choice)
    if choice == 1:
        while True:
            print("Geben Sie den Betrag ein den Sie Einzahlen wollen:")
            deposit = input()
            deposit = int(deposit)
            if deposit >= 0:
                balance += deposit
                break
            else:
                print("Der Betrag muss über 0 liegen.")
    elif choice == 2:
        while True:
            print("Geben Sie den Betrag ein den Sie Auszahlen wollen:")
            payout = input()
            payout = int(payout)
            if payout >= 0:
                if payout <= balance:
                    balance -= payout
                    break
                else:
                    print("Der Betrag den Sie auszahlen wollen ist größer als Ihr Guthaben.")
            else:
                print("Der Betrag muss über 0 liegen.")
    elif choice == 3:
        print("Der Kontostand beträgt " + str(balance) + " €")
    elif choice == 4:
        print("Auf wiedersehen")
        break
    else:
        print("Geben Sie 1, 2, 3 oder 4 ein.")
