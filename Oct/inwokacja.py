from string import ascii_lowercase
import string

with open("inwokacja.txt", "r") as plik:
    # print(plik.read())

    tekst = plik.read()

    ileSpol = 0
    ileSamo = 0
    ileLiterW = 0
    ileLiterM = 0
    ileAll = 0
    ileBialych = 0
    ileInnych = 0

    alfabet = string.ascii_letters
    print(alfabet)

    for litera in alfabet:
 
        ileAll += tekst.lower().count(litera)
        ile = tekst.count(litera)

        print(f"{litera} występuje {ile}")



    inneZnaki = [",", ".", " ", "\t", "\n", "!", "(", ")", "-"]

    for inne in inneZnaki:
        ileInnych + tekst.lower().count(inne)
        ileSpecjalnych = tekst.count(inne)
        print(f"{inne} występuje {ileSpecjalnych}")

 
#    polskieLitery = ["ą", "ę", "ć", "ł", "ń", "ś", "ż", "ź"]
#
#    for polskie in polskieLitery:
#
#        ileInnych + tekst.lower().count(polskie)
#        ilePolskich = tekst.count(polskie)
#
#        print(f"{polskie} występuje {ilePolskich}")

    




    