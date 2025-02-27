import datetime
import math

def oblicz_fale(dni: int) -> dict:
    """Oblicza wartości fal biorytmicznych dla danego dnia."""
    return {
        'fizyczna': math.sin((2 * math.pi / 23) * dni),
        'emocjonalna': math.sin((2 * math.pi / 28) * dni),
        'intelektualna': math.sin((2 * math.pi / 33) * dni)
    }

def main():
    imie = input('Jak masz na imię? ')
    try:
        dzien = int(input('Którego dnia masz urodziny? '))
        miesiac = int(input('Którego miesiąca masz urodziny? '))
        rok = int(input('Którego roku masz urodziny? '))
        urodziny = datetime.date(rok, miesiac, dzien)
    except ValueError:
        print("Błędne dane. Upewnij się, że wprowadzasz poprawne liczby.")
        return
    
    dzisiejsza_data = datetime.date.today()
    dni_od_narodzin = (dzisiejsza_data - urodziny).days
    fale_dzis = oblicz_fale(dni_od_narodzin)
    fale_jutro = oblicz_fale(dni_od_narodzin + 1)
    
    print(f'\nWitaj, {imie}!')
    print(f'Twoje urodziny były {dni_od_narodzin} dni temu.')
    print('Twoje fale biorytmiczne dzisiaj:')
    for nazwa, wartosc in fale_dzis.items():
        print(f' {nazwa.capitalize()}: {wartosc:.2f}')
    
    if all(w > 0.5 for w in fale_dzis.values()):
        print('Gratuluję dobrego wyniku!')
    elif any(w < 0.5 for w in fale_dzis.values()):
        print('Nie przejmuj się :(')
        if any(fale_jutro[n] > fale_dzis[n] for n in fale_dzis):
            print("Nie martw się. Jutro będzie lepiej!")

if __name__ == "__main__":
    main()

# Spędzony czas: 2 min