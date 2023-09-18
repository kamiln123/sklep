#zaloguj się co chcesz zrobić (obsługa kasy(sprzedaż), zmiana cen, dodanie do magazynu, inwentaryzacja, rozliczenie (przychody, dochody, wydatki), typy klientów)
#zmienić w inputach capitalize lower itd.

magazyn_cena={'Banany': 5, 'Jabłka': 4, 'Winogron': 15}
magazyn_stan={'Banany':2, 'Jabłka': 5, 'Winogron': 0}
towar=['Banany', 'Jabłka', 'Winogron']
przychód=0
sprzedane={}

def spis_cen():
    print('\n-------------')
    for i in magazyn_cena:
        print(f'{i} - {magazyn_cena[i]} zł/kg')
    print('-------------\n')

def spis_stan():
    print('\n-------------')
    for i in magazyn_stan:
        print(f'{i} - {magazyn_stan[i]} kg')
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
        if cena=='cennik':
            spis_cen()
        elif cena.isdigit()==False:
            print('Wprowadź poprawną cenę produktu')
        else:
            break
    do_zapłaty=int(kg)*int(cena)
    print(f'Sprzedawca: Do zapłaty {do_zapłaty}zł')
    print('Klient: Dziękuję, do widzenia')
    print('Sprzedawca: Do widzenia')
    global przychód
    przychód+=(do_zapłaty)
    menu()

def klient():
    from random import randint
    print('Oto pierwszy klient')
    print('Klient: Dzień dobry')
    print('Sprzedawca: Dzień dobry, co podać?')
    waga=randint(1,10)
    produkt=towar[randint(0,len(towar)-1)]
    print(f'Klient: Poproszę {waga} kg {produkt}')
    if produkt in sprzedane:
        sprzedane[produkt]+=waga
    else:
        sprzedane[produkt]=waga
    kasa()

def logowanie_kasa():
    print('Dzień dobry, kasa została podłączona do sieci')
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

def mag_cena():
    spis_cen()
    while True:
        produkt=input('Podaj nazwę produktu, którego cenę chcesz zmienić: ')
        if produkt not in magazyn_cena:
            print('Nie ma takiego produktu, wpisz ponownie')
            spis_cen()
        else:
            break
    while True:
        cena=input('Podaj cenę produktu za którą chcesz sprzedawać: ')
        if cena.isdigit()==False:
            print('Podaj kwotę za kg')
        else:
            break
    magazyn_cena[produkt]=int(cena)
    print(f'Zmieniono cenę {produkt} na {magazyn_cena[produkt]} zł/kg')
    spis_cen()
    magazyn()
    
def mag_stan():
    while True:
        stan=input('Jeżeli produkt jest już na stanie wpisz zwiększ, aby zwiększyć ilość lub dodaj, aby dodać nowy produkt, aby zakończyć wpisz zakończ: ')
        if stan=='zakończ':
            magazyn()
        elif stan=='zwiększ':
            mag_zwiększ()
        elif stan=='dodaj':
            mag_dodaj()
        else:
            print('Błąd, wybierz ponownie z listy!')

def mag_zamknij():
    while True:
        zamknij=input('Jeżeli chcesz kontynuować dostawę wpisz kontynuuj, aby zakończyć dostawę wpisz zakończ: ')
        if zamknij=='kontynuuj':
            mag_stan()
        elif zamknij=='zakończ':
            print('Zakończono dostawę')
            magazyn()
        else:
            print('Błąd, wpisz ponownie')

def mag_zwiększ():
    while True:
        produkt=input('Wybierz produkt, którego ilość chcesz zwiększyć: ')
        if produkt in magazyn_stan:
            while True:
                zwiększ=input('Podaj, ilość towaru, którą chcesz dodać: ')
                if zwiększ.isdigit()==True:
                    magazyn_stan[produkt]=magazyn_stan[produkt]+int(zwiększ)
                    print('Prawidłowe dodanie do magazynu')
                    print(f'Zmieniono stan {produkt} na {magazyn_stan[produkt]} kg')
                    mag_zamknij()
                else:
                    print('Podaj ilość w kg')
        elif produkt not in magazyn_stan:
            print('Produktu nie ma jeszcze na stanie, jeżeli chcesz go dodać przejdź do dodaj lub sprawdź ponownie stan')
            spis_stan()
            print('Wpisz ponownie co chcesz zrobić')
            mag_stan()
                    
def mag_dodaj():
    while True:
        produkt=input('Wpisz nazwę produktu który chcesz dodać: ')
        if produkt in magazyn_stan:
            print('Produkt już znajduje się w magazynie')
            mag_stan()
        else:
            break
    while True:
        cena=input('Podaj cenę za 1 kg: ')
        if cena.isdigit()==False:
            print('Cena musi być liczbą')
        else:
            break
    while True:
        ilość=input('Podaj ilość kg, które chcesz dodać: ')
        if ilość.isdigit()==False:
            print('Podaj liczbę w kg')
        else:
            break
    magazyn_cena[produkt]=int(cena)
    magazyn_stan[produkt]=int(ilość)
    towar.append(produkt)
    print(f'Pomyślnie dodano {produkt}, po cenie {magazyn_cena[produkt]} zł/kg w ilości {magazyn_stan[produkt]} kg')
    mag_zamknij()
        
def magazyn():
    while True:
        print('Wybierz działanie: zmiana cen, stan towaru, dostawa, powrót')
        mag=input()
        if mag=='zmiana cen':
            mag_cena()
        elif mag=='stan towaru':
            spis_stan()
        elif mag=='dostawa':
            spis_stan()
            print('Dostawa gotowa do przyjęcia')
            mag_stan()
        elif mag=='powrót':
            menu()
        else:
            print('Błędne dane, wpisz ponownie')
       
def menu():
    while True:
        menu=input('Wybierz co chcesz zrobić. Zalogować do kasa, magazyn, inwentaryzacja, rozliczenie lub zamknij, aby zakończyć: ')
        if menu =='kasa':
            print('Poprawne logowanie do kasa')
            logowanie_kasa()
            break
        elif menu =='magazyn':
            print('Poprawne logowanie do magazyn')
            magazyn()
            break
        elif menu =='inwentaryzacja':
            spis_stan()
        elif menu =='rozliczenie':
            print('\n-------------')
            print(f'W kasie jest {przychód}zł')
            print('Sprzedano:')
            for i in sprzedane:
                print(f'{sprzedane[i]} kg {i}')
            print('-------------\n')
        elif menu =='zamknij':
            print(f'Dzisiejszy przychód to {przychód}zł')
            print('Wylogowywanie...')
            exit()
        else:
            print('Błędne dane, proszę powtórnie wybrać profil')

     
menu()