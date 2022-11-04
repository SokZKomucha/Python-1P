# Listy imion
imiona1 = ["Anna", "Cecylia", "Bartosz", "Robert"]
imiona2 = ["Anna", "Zenon"]

# Dodawanie imion
imiona2.append("Krzysztof")
print(imiona2)

# Wstawianie elementów na istniejące
imiona2.insert(0, "Natalia")
imiona2.insert(2, "Gabriel")

wszystkieImiona = imiona1 + imiona2

# Wypisuje wszystkie elementy obu list, nie zważając na powtórzenia
print(wszystkieImiona)

# Tworzy listę eliminującą powtórzenia
wszystkieImionaBezPowtorzen = list(set(imiona1 + imiona2))

# Wypisuje już prawidłowo
print(wszystkieImionaBezPowtorzen)

# # # # # # # # #

# Sortowanie alfabetyczne
posortowane = sorted(wszystkieImionaBezPowtorzen)
print(posortowane)

# Sortowanie odwrotne
posortowaneR = sorted(wszystkieImionaBezPowtorzen, reverse=True)
print(posortowaneR)

# Wypisuje pierwszy element (element[0])
print(posortowaneR[0])
