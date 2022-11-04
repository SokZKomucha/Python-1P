n = int(input("Podaj N:\t"))
wektor = []

for i in range(n):
    liczba  = int(input("Podaj wartość:\t"))
    wektor.append(liczba)

max = wektor[0]

for i in range(1,n):
    if max < wektor[i]:
        max = wektor[i]

print(f"wektor = {wektor}")
print(f"max = {max}")