
import random

decPasswordList = []                                    # Lista przechowująca liczby odpowiadające poszczególnym charom
txtPasswordList = []                                    # Lista przechowująca chary hasła
passwordLength = int(input("Podaj długość hasła -\t"))  # Przechowuje informację o długości hasła
decPasswordGen = 0                                      # Zmienna do pętli pierwszej
txtPasswordGen = 0                                      # Zmienna do pętli drugiej
charToPass = 0                                          # Zmienna do pętli trzeciej
password = ""                                           # Gotowe hasło

# Pętla generująca liczby, które zostaną przypisane charom
# Da się zrobić lepiej, ja wiem
# Niestety jednak jestem początkujący
while (decPasswordGen < passwordLength):
    decPasswordList.append(random.randint(36, 126))
    decPasswordGen += 1

# Pętla generująca chary z liczb powyżej
while (txtPasswordGen < passwordLength):
    txtPasswordList.append(chr(decPasswordList[txtPasswordGen]))
    txtPasswordGen += 1

# Miesza te chary
random.shuffle(txtPasswordList)

# Pętla przypisująca znaki hasłu
while (charToPass < passwordLength):
    password += txtPasswordList[charToPass]
    charToPass += 1

print (password)



# - Generuje hasło z liczb, liter małych/wielkich oraz znaków specjalnych
# - Liczby do zamiany są generowane losowo (od 36 do 126)
# - Liczby te są potem zamieniane na znaki
# - Tablica z tymi znakami jest mieszana 
# - Hasło jest tworzone z tych znaków
# - Hasło jest wypisywane