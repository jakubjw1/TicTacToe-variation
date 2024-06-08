
plansza = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

przegrywajace_kombinacje = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def czy_przegrany(plansza):
    for a, b, c in przegrywajace_kombinacje:
        if plansza[a] == plansza[b] == plansza[c] == 'X':
            return True
    return False

def rysuj_plansze(plansza):
    print('-------------')
    print('| ' + plansza[0] + ' | ' + plansza[1] + ' | ' + plansza[2] + ' |')
    print('-------------')
    print('| ' + plansza[3] + ' | ' + plansza[4] + ' | ' + plansza[5] + ' |')
    print('-------------')
    print('| ' + plansza[6] + ' | ' + plansza[7] + ' | ' + plansza[8] + ' |')
    print('-------------')

def dostepne_pola(plansza):
    return [i for i in range(9) if plansza[i] == ' ']

def minimax(maksymalizacja, plansza):
    if czy_przegrany(plansza):
        return -1
    elif all(pole != ' ' for pole in plansza):
        return 0

    if maksymalizacja:
        najlepszy_wynik = -float('inf')
        for pole in dostepne_pola(plansza):
            plansza[pole] = 'X'
            wynik = minimax(False, plansza)
            plansza[pole] = ' '
            najlepszy_wynik = max(wynik, najlepszy_wynik)
        return najlepszy_wynik
    else:
        najlepszy_wynik = float('inf')
        for pole in dostepne_pola(plansza):
            plansza[pole] = 'X'
            wynik = minimax(True, plansza)
            plansza[pole] = ' '
            najlepszy_wynik = min(wynik, najlepszy_wynik)
        return najlepszy_wynik

def ruch_komputera(plansza):
    najlepszy_wynik = -float('inf')
    najlepsze_pole = None
    for pole in dostepne_pola(plansza):
        plansza[pole] = 'X'
        if czy_przegrany(plansza):
            plansza[pole] = ' '
            continue
        wynik = minimax(False, plansza)
        plansza[pole] = ' '
        if wynik > najlepszy_wynik:
            najlepszy_wynik = wynik
            najlepsze_pole = pole
    if najlepsze_pole is None:
        najlepsze_pole = dostepne_pola(plansza)[0]
    plansza[najlepsze_pole] = 'X'
    print("Komputer wybrał pole: ", najlepsze_pole)
    return plansza

def ruch_gracza(plansza):
    while True:
        try:
            pole = int(input('Wybierz dostępne pole na planszy wpisując odpowiedni numer (0-8): '))
            while pole > 8 or pole < 0 or plansza[pole] == 'X':
                pole = int(input('Wpisałeś nieprawidłową wartość lub to pole jest już zajęte.\n'
                                 'Wybierz dostępne pole na planszy wpisując odpowiedni numer (0-8): '))
            plansza[pole] = 'X'
            return plansza
        except ValueError:
            print("To nie jest liczba. Wpisz liczbę z zakresu 0-8.")

def graj():
    czy_zaczynam = input("Czy chcesz zacząć grę (t/n): ")
    while czy_zaczynam != 't' and czy_zaczynam != 'n':
        czy_zaczynam = input("Czy chcesz zacząć grę (t/n): ")
    if czy_zaczynam.lower() == 't':
        kolej_gracza = True
    else:
        kolej_gracza = False

    print('-------------')
    print('| 0 | 1 | 2 |')
    print('-------------')
    print('| 3 | 4 | 5 |')
    print('-------------')
    print('| 6 | 7 | 8 |')
    print('-------------')

    while True:
        if kolej_gracza:
            ruch_gracza(plansza)
            rysuj_plansze(plansza)
            if czy_przegrany(plansza):
                print("Przegrałeś!")
                break
            kolej_gracza = False
        else:
            ruch_komputera(plansza)
            rysuj_plansze(plansza)
            if czy_przegrany(plansza):
                print("Wygrałeś!")
                break
            kolej_gracza = True

graj()