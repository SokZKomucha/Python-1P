import base64

msgHex = "2e2e3f9dabbcfc16c5f0fb5ee00b"     # Message hex
keyHex = "584b51f48bca9572acd08d378362"     # Key hex

msgBin = ( bin(int(msgHex, 16))[2:] ).zfill( len(msgHex) * 4 )      # Message bin
keyBin = ( bin(int(keyHex, 16))[2:] ).zfill( len(keyHex) * 4 )      # Key bin
xorBin = ""                                                         # Xor bin

loopNm = 0  # Something used in the loop

# XORs both strings by comparing a[i] and b[i] contents
#   A   B   OUT
#   0   0   0
#   1   0   1
#   0   1   1
#   1   1   0

while (loopNm < len(msgBin) and len(msgBin) == len(keyBin)):

    if (msgBin[loopNm] == "0" and keyBin[loopNm] == "0"):
        xorBin += "0"
    elif (msgBin[loopNm] == "1" and keyBin[loopNm] == "0"):
        xorBin += "1"
    elif (msgBin[loopNm] == "0" and keyBin[loopNm] == "1"):
        xorBin += "1"
    elif (msgBin[loopNm] == "1" and keyBin[loopNm] == "1"):
        xorBin += "0"

    loopNm += 1



xorDec = int(xorBin, 2)                 # Converts bin XOR to dec XOR
xorHex = str(hex(xorDec)).upper()[2:]   # Converts dec XOR to hex XOR string 
#         ^   ^   ^        ^      ^
# Strings it  |   |        |      |
# Converts to hex |        |      |
# This is being converted  |      |
# Converts all chars to uppercase |
# Deletes first two characters ("0x")

# Stores converted string
textConverted = base64.b16decode(xorHex)



# Message hex   Key hex
#           |   |
#   
# Message bin   key bin
#           |   |
#            \ /
#             |
#   
#          xor bin
#             |
#
#          xor dec
#             |         converts it to string, uppercases all characters, deletes first two characters ("0x")
#
#          xor hex
#             |         decodes it using base16 decode
#
#       textConverted

# Output - " b'veni vidi vici' "
#
# Wystarczy mojego słabego angielskiego; 
# Funkcja dekodowania zwraca nam wynik w postaci ``` b'[wynik]' ``` (z tym b oraz ')
# Nie, nie jest to błąd w programie. Działanie funkcji było testowawne przy użyciu
# innego stringa hexów, "4B6F6D7075746572" (tj. "Komputer").
# 
# Z tego powodu warto by usunąć pierwsze dwa znaki oraz ostatni jeden z wyniku.
# Niestety tego nie zrobiłem, bo z jakiegoś powodu nie działa.
#
# Ale program generalnie działa, zwraca nam poprawnie zdekodowany tekst
# A "Jak coś działa to nie jest głupie" 

print(f"msgBin -\t {msgBin}")           # zwraca msgBin
print(f"keyBin -\t {keyBin}")           # zwraca keyBin
print(f"xorBin -\t {xorBin}")           # zwraca xorBin
print(f"xorHex -\t {xorHex}")           # zwraca xorHex
print(f"txtNcr -\t {textConverted}")    # zwraca zdekodowany tekst

# Cały program zmieścił się w stu linijkach. Na dysku nawet
# nie zajmuje 5KB, więc powiedziałbym, że to dobry znak.