# Pesel składa się z 11 cyfr


# Wagi każdej z cyfr  -  
#   1   2   3   4   5   6   7   8   9   10  11
#   1   3   7   9   1   3   7   9   1   3   -

# Jak sprawdzić, czy pesel jest prawidłowy?
# - Sumujemy wynik mnożenia każdej z 10 cyfr przez odpowiadającą jej wagę
# - Wynik dzielimy przez 10
# - Jeśli wyjdzie 0, to liczbą kontrolną jest 0
# - Jeśli wyjdzie co innego, wykonujemy działanie. Wynik dzielenia odejmujemy od 10



peselInput = str(input("Wprowadź pesel: "))

peselRozmiar = len(peselInput)

if peselRozmiar == 11: 
    pesel1 = peselInput[0]
    pesel2 = peselInput[1]
    pesel3 = peselInput[2]
    pesel4 = peselInput[3]
    pesel5 = peselInput[4]
    pesel6 = peselInput[5]
    pesel7 = peselInput[6]
    pesel8 = peselInput[7]
    pesel9 = peselInput[8]
    pesel10 = peselInput[9]
    Kontrolna = peselInput[10]

    pesel1 = pesel1 * 1
    pesel2 = pesel2 * 3
    pesel3 = pesel3 * 7
    pesel4 = pesel4 * 9

    pesel5 = pesel5 * 1
    pesel6 = pesel6 * 3
    pesel7 = pesel7 * 7
    pesel8 = pesel8 * 9

    pesel9 = pesel9 * 1
    pesel10 = pesel10 * 3

    suma1do10 = pesel1 + pesel2 + pesel3 + pesel4 + pesel5 + pesel6 + pesel7 + pesel8 + pesel9 + pesel10

    print(suma1do10)











