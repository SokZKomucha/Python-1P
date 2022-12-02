import time # sleep

windSpeed = float(input("Podaj predkosc wiatru w km/h -\t"))

if (windSpeed < 5):
    print("0 w skali Beauforta; cisza.")

elif (windSpeed >= 5 and windSpeed < 11):
    print("1 w skali Beauforta; powiew.")

elif (windSpeed >= 11 and windSpeed < 19):
    print("2 w skali Beauforta; slaby wiatr.")

elif (windSpeed >= 19 and windSpeed < 28):
    print("3 w skali Beauforta; lagodny wiatr.")

elif (windSpeed >= 28 and windSpeed < 38):
    print("4 w skali Beauforta; umiarkowany wiatr.")

elif (windSpeed >= 38 and windSpeed < 49):
    print("5 w skali Beauforta; dosyc silny wiatr.")

elif (windSpeed >= 49 and windSpeed < 61):
    print("6 w skali Beauforta; silny wiatr.")

elif (windSpeed >= 61 and windSpeed < 74):
    print("7 w skali Beauforta; bardzo silny wiatr.")

elif (windSpeed >= 74 and windSpeed < 88):
    print("8 w skali Beauforta; sztorm.")

elif (windSpeed >= 88 and windSpeed < 102):
    print("9 w skali Beauforta; silny sztorm.")

elif (windSpeed >= 102 and windSpeed < 117):
    print("10 w skali Beauforta; bardzo silny sztorm.")

elif (windSpeed >= 117 and windSpeed < 118):
    print("11 w skali Beauforta; gwaltowny sztorm.")

elif (windSpeed >= 118):
    print("12 w skali Beauforta; huragan.")

time.sleep(5)