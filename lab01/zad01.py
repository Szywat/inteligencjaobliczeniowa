import datetime
import math

imie = input('Jak masz na imię? ')
dzien = int(input('Którego dnia masz urodziny? '))
miesiac = int(input('Którego miesiąca masz urodziny? '))
rok = int(input('Którego roku masz urodziny? '))

urodziny = datetime.datetime(rok, miesiac, dzien)
dzisiejsza_data = datetime.datetime.now()

print(dzisiejsza_data)

dni_od_narodzin = (dzisiejsza_data - urodziny).days

yP = math.sin((2*math.pi / 23)* dni_od_narodzin)
yE = math.sin((2*math.pi / 28)* dni_od_narodzin)
yI = math.sin((2*math.pi / 33)* dni_od_narodzin)

nastepny_dzien = dni_od_narodzin + 1

nextYP = math.sin((2*math.pi / 23)* nastepny_dzien)
nextYE = math.sin((2*math.pi / 28)* nastepny_dzien)
nextYI = math.sin((2*math.pi / 33)* nastepny_dzien)

print(f'Witaj {imie}')
print(f'Twoje urodziny były tyle dni temu: {dni_od_narodzin} ')
print('Twoje fale:')
print(f' Fizyczna fala: {yP}')
print(f' Emocjonalna fala: {yE}')
print(f' Intelektualna fala: {yI}')

if yP > 0.5 and yE > 0.5 and yI > 0.5:
    print('Gratuluję dobrego wyniku!')
elif yP < 0.5 or yE < 0.5 or yI < 0.5:
    print('Nie przejmuj się :(')
    if nextYP > yP or nextYE > yE or nextYI > yI:
        print("Nie martw się. Jutro będzie lepiej!")

# Spędzony czas: 1.5 - 2h