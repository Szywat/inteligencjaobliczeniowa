import datetime
import math

imie = input('Jak masz na imię? ')
dzien = int(input('Którego dnia masz urodziny? '))
miesiac = int(input('Którego miesiąca masz urodziny? '))
rok = int(input('Którego roku masz urodziny? '))

urodziny = datetime.datetime(rok, miesiac, dzien)
dzisiejsza_data = datetime.datetime.now()

print(dzisiejsza_data)

dni_do_narodzin = (dzisiejsza_data - urodziny).days

yP = math.sin((2*math.pi / 23)* dni_do_narodzin)
yE = math.sin((2*math.pi / 28)* dni_do_narodzin)
yI = math.sin((2*math.pi / 33)* dni_do_narodzin)

print(f'Witaj {imie}')
print(f'Twoje urodziny były tyle dni temu: {dni_do_narodzin} ')
print('Twoje fale:')
print(f' Fizyczna fala: {yP}')
print(f' Emocjonalna fala: {yE}')
print(f' Intelektualna fala: {yI}')
