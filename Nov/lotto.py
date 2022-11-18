
import random

kasa = 15

while True:
    trafione = 0

    l1 = random.randint(0, 49)
    l2 = random.randint(0, 49)
    l3 = random.randint(0, 49)
    l4 = random.randint(0, 49)
    l5 = random.randint(0, 49)
    l6 = random.randint(0, 49)



    while l2 == l1 or l2 == l3 or l2 == l4 or l2 == l5 or l2 == l6:
        l2 = random.randint(0, 49)

    while l3 == l1 or l3 == l4 or l3 == l5 or l3 == l6:
        l3 = random.randint(0, 49)

    while l4 == l1 or l4 == l5 or l4 == l6:
        l4 = random.randint(0, 49)

    while l5 == l1 or l5 == l6:
        l5 = random.randint(0, 49)

    while l6 == l1:
        l6 = random.randint(0, 49)

    print(f"{l1}, {l2}, {l3}, {l4}, {l5}, {l6}")

    print("\nWpisz 6 różnych liczb:\n")
    c1 = int(input("Podaj liczbę 1 -\t"))
    c2 = int(input("Podaj liczbę 2 -\t"))
    c3 = int(input("Podaj liczbę 3 -\t"))
    c4 = int(input("Podaj liczbę 4 -\t"))
    c5 = int(input("Podaj liczbę 5 -\t"))
    c6 = int(input("Podaj liczbę 6 -\t"))



    if l1 == c1:
        trafione = trafione + 1

    if l2 == c2:
        trafione = trafione + 1
        
    if l3 == c3:
        trafione = trafione + 1

    if l4 == c4:
        trafione = trafione + 1

    if l5 == c5:
        trafione = trafione + 1

    if l6 == c6:
        trafione = trafione + 1   



    if trafione == 0:
        kasa = kasa - 5
        print("Rip bozo")

    elif trafione == 1:
        kasa = kasa - 5

    elif trafione == 2:
        kasa = kasa - 5

    elif trafione == 3:
        kasa = kasa - 5
        kasa = kasa + 10

    elif trafione == 4:
        kasa = kasa - 5 
        kasa = kasa + 1000

    elif trafione == 5:
        kasa = kasa - 5
        kasa = kasa + 3500 

    elif trafione == 6:
        kasa = kasa - 5
        kasa = kasa + 1000000

    print(f"\nTrafione - {trafione}\nBudżet - {kasa}\n\n")
