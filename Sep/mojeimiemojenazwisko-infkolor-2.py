def koloruj(k,text):
    return f"\033[{k}m{text}\033[0m"

n = int(input("podaj liczbe:\t"))

for x in range(1,n+1):
    for y in range(1,n+1):
        
        wynik = x * y

        if wynik < 10:
            print(koloruj(91,wynik),end="\t")
        elif wynik >= 10 and wynik < 20:
            print(koloruj(92,wynik),end="\t")
        elif wynik >= 20 and wynik < 30:
            print(koloruj(93,wynik),end="\t")
        else:
            print(wynik,end="\t")
    print()

    # Program nie działał prawidłowo przez to, że warunki były ustawione źle 
    # (nie był dany jakiś zakres, tylko ``liczba > x``, przez co kolor się nakładały)

    # Naprawione, od teraz liczby 1-9 powinny być wyświetlane w jednym kolorze, 
    # liczby 10-19 w drugim, liczby 20-30 w trzecim, większe w innym

    # Niestety nie bardzo znam mechamizn zmiany koloru tekstu, ale generalnie 
    # zakresy powinny być już naprawione.
