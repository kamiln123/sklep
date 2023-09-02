#zaloguj się co chcesz zrobić (obsługa kasy(sprzedaż), zmiana cen, dodanie do magazynu, inwentaryzacja, rozliczenie (przychody, dochody, wydatki), typy klientów)

def spis_cen():
    print(f"""
          Banany- 5zł/kg
          Jabłka- 4zł/kg
          Winogron- 15zł/kg
          """)

def kasa():
    while True:
        kg=input('Wpisz wagę: ')
        if kg.isdigit()==False:
            print('Wprowadź wagę w kilogramach!')
        else:
            break
    while True:
        cena=input('Wprowadź cenę za kg: ')
        if cena.isdigit()==False:
            print('Wprowadź poprawną cenę produktu')
        else:
            break
    print(f'Do zapłaty {int(kg)*int(cena)}zł')
    print('Dziękuję, do widzenia')
    
def klient():
    from random import randint
    towar=['bananów', 'jabłek', 'winogron']
    print('Oto pierwszy klient')
    print('Klient: Dzień dobry')
    print('Sprzedawca: Dzień dobry, co podać?')
    print(f'Poproszę {randint(1,10)} kg {towar[randint(0,2)]}')
    kasa()

def logowanie_kasa():
    print('Dzień dobry kasa została podłączona do sieci')
    while True:
        cennik=input('Aby poznać cenę towarów wpisz "cennik" lub aby wyjść "wyjście": ')
        if cennik =='cennik':
            spis_cen()
            break
        elif cennik=='wyjście':
            break
        else:
            print('Brak danych, proszę powtórnie wybrać polecenie')
    print('Jesteś gotowy na przyjęcie pierwszego klienta')
    klient()

while True:
    menu=input('Wybierz co chcesz zrobić. Zalogować do kasa, magazyn, inwentaryzacja, rozliczenie: ')
    if menu =='kasa':
        print('Poprawne logowanie')
        logowanie_kasa()
        break
    elif menu =='magazyn' or menu =='inwentaryzacja' or menu =='rozliczenie':
        print('Wkrótce dostępne')
    else:
        print('Błędne dane, proszę powtórnie wybrać profil')
        
