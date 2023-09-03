#zaloguj się co chcesz zrobić (obsługa kasy(sprzedaż), zmiana cen, dodanie do magazynu, inwentaryzacja, rozliczenie (przychody, dochody, wydatki), typy klientów)
#zmienić w inputach capitalize lower itd.

magazyn_cena={'Banany': 5, 'Jabłka': 4, 'Winogron': 15}
magazyn_stan={}

def spis_cen():
    print('\n-------------')
    for i in magazyn_cena:
        print(f'{i} - {magazyn_cena[i]}/kg')
    print('-------------\n')

def kasa():
    while True:
        kg=input('Wpisz wagę: ')
        if kg.isdigit()==False:
            print('Wprowadź wagę w kilogramach!')
        else:
            break
    while True:
        cena=input('Wprowadź cenę za kg, jeżeli nie pamiętasz ceny wpisz ponownie cennik: ')
        if cena.isdigit()==False:
            print('Wprowadź poprawną cenę produktu')
        if cena=='cennik':
            spis_cen()
        else:
            break
    print(f'Do zapłaty {int(kg)*int(cena)}zł')
    print('Dziękuję, do widzenia')
    exit()

def mag_cena():
    spis_cen()
    while True:
        produkt=input('Podaj nazwę produktu, którego cenę chcesz zmienić: ')
        if produkt not in magazyn_cena:
            print('Nie ma takiego produktu, wpisz ponownie')
            print(spis_cen())
        else:
            break
    while True:
        cena=input('Podaj cenę produktu za którą chcesz sprzedawać: ')
        if cena.isdigit()==False:
            print('Podaj kwotę za kg')
        else:
            break

    magazyn_cena[produkt]=int(cena)
    print(f'Zmieniono cenę {produkt} na {magazyn_cena[produkt]}zł')
    spis_cen()
    magazyn()
    
def magazyn():
    while True:
        print('Wybierz działanie: zmiana cen, stan towaru, dostawa, powrót')
        mag=input()
        if mag=='zmiana cen':
            mag_cena()
        elif mag=='stan towaru':
            print('Wkrótce dostępne')
        elif mag=='dostawa':
            print('Wkrótce dostępne')
        elif mag=='powrót':
            menu()
        else:
            print('Błędne dane, wpisz ponownie')
       
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

def menu():
    while True:
        menu=input('Wybierz co chcesz zrobić. Zalogować do kasa, magazyn, inwentaryzacja, rozliczenie: ')
        if menu =='kasa':
            print('Poprawne logowanie do kasa')
            logowanie_kasa()
            break
        elif menu =='magazyn':
            print('Poprawne logowanie do magazyn')
            magazyn()
            break
        elif menu =='inwentaryzacja' or menu =='rozliczenie':
            print('Wkrótce dostępne')
        else:
            print('Błędne dane, proszę powtórnie wybrać profil')
        
menu()