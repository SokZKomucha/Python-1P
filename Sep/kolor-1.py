def koloruj(k,text):
    return f"\033[{k}m{text}\033[0m"

n = int(input("podaj liczbe:\t"))

for x in range(1,n+1):
    for y in range(1,n+1):
        
        wynik = x * y

        if wynik < 10:
            print(koloruj(91,wynik),end="\t")
        elif wynik < 20:
            print(koloruj(92,wynik),end="\t")
        elif wynik < 30:
            print(koloruj(93,wynik),end="\t")
        else:
            print(wynik,end="\t")
    print()