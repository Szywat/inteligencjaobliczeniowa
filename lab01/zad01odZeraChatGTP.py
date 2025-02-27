import math
import datetime

def calculate_biorhythm(days_lived, cycle):
    return math.sin(2 * math.pi * days_lived / cycle)

def main():
    name = input("Podaj swoje imię: ")
    year = int(input("Podaj rok urodzenia: "))
    month = int(input("Podaj miesiąc urodzenia: "))
    day = int(input("Podaj dzień urodzenia: "))
    
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    
    days_lived = (today - birth_date).days
    
    physical = calculate_biorhythm(days_lived, 23)
    emotional = calculate_biorhythm(days_lived, 28)
    intellectual = calculate_biorhythm(days_lived, 33)
    
    next_physical = calculate_biorhythm(days_lived + 1, 23)
    next_emotional = calculate_biorhythm(days_lived + 1, 28)
    next_intellectual = calculate_biorhythm(days_lived + 1, 33)
    
    print(f"\nWitaj, {name}!")
    print(f"Dziś jest {days_lived} dzień Twojego życia.")
    print(f"Twój biorytm:")
    
    for label, value, next_value in [("Fizyczny", physical, next_physical),
                                      ("Emocjonalny", emotional, next_emotional),
                                      ("Intelektualny", intellectual, next_intellectual)]:
        print(f"- {label}: {value:.2f}")
        if value > 0.5:
            print(f"  Gratulacje! Masz wysoki wynik w kategorii {label}.")
        elif value < -0.5:
            print(f"  Nie przejmuj się, masz niski wynik w kategorii {label}.")
            if next_value > value:
                print("  Nie martw się. Jutro będzie lepiej!")

if __name__ == "__main__":
    main()

# Spędzony czas: 8 min