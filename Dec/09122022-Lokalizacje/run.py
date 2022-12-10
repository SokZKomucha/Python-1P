import os 

        # Nazwa pliku
with open("informacje.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    for i in range(len(lines)):

        lines[i] = lines[i][0:-1]
        klasa, grupa, imie = lines[i].split("_")

        try:
            os.makedirs(fr"{klasa}\{grupa}\{imie}")
        except FileExistsError:
            pass

 