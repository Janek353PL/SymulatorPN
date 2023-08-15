import random

druzyny_plik = open(r"druzyny.txt", 'r')
wynik_plik = open(r"wynik.txt", 'w')
pilkarze = [[''] * 11, [''] * 11]
poz = [[''] * 11, [''] * 11]
ovr = [[0] * 11, [0] * 11]
obrona = [0, 0]
obronastat = [[0] * 11, [0] * 11]
atak = [0, 0]
atakstat = [[0] * 11, [0] * 11]
pomoc = [0, 0]
pomocstat = [[0] * 11, [0] * 11]
asysta = [0, 0]
asystastat = [[0] * 11, [0] * 11]
kartka = [0, 0]
kartkastat = [[0] * 11, [0] * 11]
ocena = [[6.6] * 11, [6.6] * 11]
kartkailo = [[0] * 11, [0] * 11]
status = [[''] * 11, [''] * 11]
typ_meczu = ''
bonus_boiska = 0
wynik_dwumeczu = [0, 0]
nazwa = ['', '']
trenerzy = ['', '']
trener_ovr = [[0] * 3, [0] * 3]
szanse = [0, 0]
posiadanie = [0, 0]
skartka = [0, 0]
bonus_boiska = 0
sredni_ovr = 0
akcje = [50, 50]
minuta = 0
minuta_str = ''
gole = [0, 0]
wynik = ''
logo = ['', '']
zmienieni = []


def dodaj_zawodnika(nr, pilkarz, pozycja, ovrn, i):
    pilkarze[nr][i] = pilkarz
    poz[nr][i] = pozycja
    ovr[nr][i] = int(ovrn)
    ocena[nr][i] = 6.6
    if (pozycja == "GK"):
        obronastat[nr][i] = 100 * ovr[nr][i]
        pomocstat[nr][i] = 0
        atakstat[nr][i] = 0
        asystastat[nr][i] = ovr[nr][i]
        kartkastat[nr][i] = 99 - ovr[nr][i]
        ocena[nr][i] = 7
    if (pozycja == "PO" or pozycja == "LO"):
        obronastat[nr][i] = 90 * ovr[nr][i]
        pomocstat[nr][i] = 1 * ovr[nr][i]
        atakstat[nr][i] = 10 * ovr[nr][i]
        asystastat[nr][i] = 40 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 75
    if (pozycja == "SO"):
        obronastat[nr][i] = 95 * ovr[nr][i]
        pomocstat[nr][i] = 5 * ovr[nr][i]
        atakstat[nr][i] = 5 * ovr[nr][i]
        asystastat[nr][i] = 5 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 100
        ocena[nr][i] = 6.8
    if (pozycja == "PP" or pozycja == "LP"):
        obronastat[nr][i] = 40 * ovr[nr][i]
        pomocstat[nr][i] = 15 * ovr[nr][i]
        atakstat[nr][i] = 60 * ovr[nr][i]
        asystastat[nr][i] = 60 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 60
    if (pozycja == "SPD"):
        obronastat[nr][i] = 70 * ovr[nr][i]
        pomocstat[nr][i] = 20 * ovr[nr][i]
        atakstat[nr][i] = 25 * ovr[nr][i]
        asystastat[nr][i] = 20 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 90
    if (pozycja == "SP"):
        obronastat[nr][i] = 50 * ovr[nr][i]
        pomocstat[nr][i] = 25 * ovr[nr][i]
        atakstat[nr][i] = 50 * ovr[nr][i]
        asystastat[nr][i] = 80 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 70
    if (pozycja == "SPO"):
        obronastat[nr][i] = 30 * ovr[nr][i]
        pomocstat[nr][i] = 22 * ovr[nr][i]
        atakstat[nr][i] = 70 * ovr[nr][i]
        asystastat[nr][i] = 100 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 50
    if (pozycja == "PS" or pozycja == "LS"):
        obronastat[nr][i] = 25 * ovr[nr][i]
        pomocstat[nr][i] = 10 * ovr[nr][i]
        atakstat[nr][i] = 75 * ovr[nr][i]
        asystastat[nr][i] = 75 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 40
    if (pozycja == "SN"):
        obronastat[nr][i] = 5 * ovr[nr][i]
        pomocstat[nr][i] = 15 * ovr[nr][i]
        atakstat[nr][i] = 95 * ovr[nr][i]
        asystastat[nr][i] = 55 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 10
    if (pozycja == "N"):
        obronastat[nr][i] = 0 * ovr[nr][i]
        pomocstat[nr][i] = 10 * ovr[nr][i]
        atakstat[nr][i] = 100 * ovr[nr][i]
        asystastat[nr][i] = 50 * ovr[nr][i]
        kartkastat[nr][i] = (99 - ovr[nr][i]) * 5
    obrona[nr] += obronastat[nr][i]
    pomoc[nr] += pomocstat[nr][i]
    atak[nr] += atakstat[nr][i]
    asysta[nr] += asystastat[nr][i]
    kartka[nr] += kartkastat[nr][i]


def usun_zawodnika(nr, i):
    atak[nr] -= atakstat[nr][i]
    atakstat[nr][i] = 0
    obrona[nr] -= obronastat[nr][i]
    obronastat[nr][i] = 0
    asysta[nr] -= asystastat[nr][i]
    asystastat[nr][i] = 0
    kartka[nr] -= kartkastat[nr][i]
    kartkastat[nr][i] = 0
    ovr[nr][i] = 0


def oblicz_szanse():
    szanse[0] = 100 * (atak[0] + (trener_ovr[0][2] * 100) + bonus_boiska) // (obrona[1] + (trener_ovr[1][0] * 100))
    szanse[1] = 100 * (atak[1] + (trener_ovr[0][2] * 100)) // (obrona[0] + (trener_ovr[0][0] * 100) + bonus_boiska)
    skartka[0] = 100 * atak[1] // obrona[0]
    skartka[1] = 100 * atak[0] // obrona[1]
    for i in range(2):
        if (szanse[i] < 0.5): szanse[i] = 0.5
        if (skartka[i] < 0.5): skartka[i] = 0.5
    print(f'Szanse na gola: {szanse[0]} - {szanse[1]}\nSzanse na kartke: {skartka[0]} - {skartka[1]}')
    oblicz_sredni_ovr()


def oblicz_posiadanie_pilki():
    posiadanie_akcja = [0, 0]
    liczba = random.randint(0, 20)
    liczba -= 10
    posiadanie_akcja[0] = int((pomoc[0] + trener_ovr[0][1] + bonus_boiska) / (pomoc[1] + trener_ovr[1][1]) * 100)
    posiadanie_akcja[1] = int((pomoc[1] + trener_ovr[1][1]) / (pomoc[0] + trener_ovr[0][1] + bonus_boiska) * 100)
    temp = posiadanie_akcja[0]
    posiadanie_akcja[0] = posiadanie_akcja[0] + posiadanie_akcja[0] * (liczba / 100)
    posiadanie_akcja[1] = posiadanie_akcja[1] + temp - posiadanie_akcja[0]
    for i in range(2):
        posiadanie[i] += posiadanie_akcja[i]


def oblicz_sredni_ovr():
    global sredni_ovr
    sredni_ovr = 0
    for j in range(2):
        for i in range(11):
            sredni_ovr += ovr[j][i]
    sredni_ovr = sredni_ovr // 22
    print(f'Średni ovr tego meczu wynosi: {sredni_ovr}')


def oblicz_minuta():
    global minuta
    global minuta_str
    obecna_akcja = akcje[0] + akcje[1]
    minuta += 1
    if obecna_akcja == 50: minuta = 46
    minuta_str = str(minuta)
    if obecna_akcja <= 55 and obecna_akcja >= 51:
        if minuta == 46:
            minuta_str = "45+1"
        elif minuta == 47:
            minuta_str = "45+2"
        elif minuta == 48:
            minuta_str = "45+3"
        elif minuta == 49:
            minuta_str = "45+4"
        elif minuta == 50:
            minuta_str = "45+5"
    if obecna_akcja <= 5 and obecna_akcja >= 1:
        if minuta == 91:
            minuta_str = "90+1"
        elif minuta == 92:
            minuta_str = "90+2"
        elif minuta == 93:
            minuta_str = "90+3"
        elif minuta == 94:
            minuta_str = "90+4"
        elif minuta == 95:
            minuta_str = "90+5"


def kontuzja(y, sz_grozna, sz_lekka, min_przedzial):
    global wynik
    liczba = random.randint(1, 100)
    i = random.randint(min_przedzial, 10)
    if (liczba <= sz_grozna):
        wynik += f"{minuta_str}' {pilkarze[y][i]}  :ambulance: {logo[y]}\n"
        print(f"\n{minuta_str}' {pilkarze[y][i]} ({poz[y][i]}) doznał poważnej kontuzji i potrzebna jest zmiana!")
        zmiana(y, i)
    elif (liczba <= sz_lekka):
        wynik += f"{minuta_str}' {pilkarze[y][i]}  :adhesive_bandage: {logo[y]}\n"
        karny_ovr = random.randint(0, 3)
        if karny_ovr != 0:
            ovr[y][i] -= karny_ovr
            print(
                f"\n{minuta_str}' {pilkarze[y][i]} ({poz[y][i]}) doznał lekkiej kontuzji i będzie grał na poziomie {ovr[y][i]} ovr")
            czy_zmiana = input('\nCzy chcesz zmienić tego zawodnika? (T/N) - ')
            while (czy_zmiana != 'T' and czy_zmiana != 'N'):
                czy_zmiana = input('Czy chcesz zmienić tego zawodnika?\nNapisz literę T lub N - ')
            if czy_zmiana == 'T':
                zmiana(y, i)


def zmiana(nr_druzyny, nr_zawodnika):
    pytanie = 'N'
    zmienieni.append([nr_druzyny, pilkarze[nr_druzyny][nr_zawodnika], ocena[nr_druzyny][nr_zawodnika]])
    usun_zawodnika(nr_druzyny, nr_zawodnika)
    while (pytanie != 'T'):
        print(f'\nWprowadź dane nowego zawodnika w formacie:\nzawodnik pozycja ovr')
        nowy_zawodnik = input()
        temp = nowy_zawodnik.strip().split()
        pilkarz = " ".join(str(x) for x in (temp[:-2]))
        print(
            f'\nCzy to poprawne dane zawodnika, które chcesz wprowadzić?\nZawodnik: {pilkarz}\nPozycja: {temp[-2]}\nOVR: {temp[-1]}')
        pytanie = input('T/N: ')
        while (pytanie != 'T' and pytanie != 'N'):
            pytanie = input('Czy to poprawne dane tego zawodnika?\nNapisz literę T lub N - ')
    dodaj_zawodnika(nr_druzyny, pilkarz, temp[-2], temp[-1], nr_zawodnika)
    oblicz_szanse()


def akcja_meczowa():
    for y in range(2):
        if (akcje[y] > 0):
            global wynik
            global minuta
            oblicz_minuta()
            akcje[y] -= 1
            if y == 0:
                z = 1
            else:
                z = 0
            liczba = random.randint(1, 100)
            if (liczba <= 5):
                liczba = random.randint(1, skartka[y] + szanse[y])
                # GOL
                if (liczba <= szanse[y]):
                    # print(liczba," ",szanse[y])
                    gole[y] += 1
                    liczba = random.randint(1, atak[y])
                    i = 0
                    x = atakstat[y][0]
                    while (x <= liczba):
                        i += 1
                        x += atakstat[y][i]
                    liczba = random.randint(1, asysta[y])
                    x = asystastat[y][0]
                    q = 0
                    while (x <= liczba):
                        q += 1
                        x += asystastat[y][q]
                    if (pilkarze[y][i] != pilkarze[y][q]):
                        wynik += f"{minuta_str}' {pilkarze[y][i]} :soccer: {logo[y]} (:busts_in_silhouette: {pilkarze[y][q]})\n"
                        ocena[y][i] += random.randint(2, 10) / 10
                        ocena[y][q] += random.randint(1, 5) / 10
                    else:
                        wynik += f"{minuta_str}' {pilkarze[y][i]} :soccer: {logo[y]} (:busts_in_silhouette: __BRAK__)\n"
                        ocena[y][i] += random.randint(2, 10) / 10
                    for i in range(11):
                        ocena[y][i] += 0.1
                        if poz[z][i] == "GK":
                            ocena[z][i] -= random.randint(3, 6) / 10
                        elif poz[z][i] == "SO":
                            ocena[z][i] -= random.randint(2, 4) / 10
                        elif poz[z][i] == "PO" or poz[z][i] == "LO" or poz[z][i] == "SPD":
                            ocena[z][i] -= random.randint(1, 2) / 10
                        else:
                            ocena[z][i] -= 0.1

                # kartka
                elif (liczba <= skartka[y] + szanse[y]):
                    i = 0
                    x = kartkastat[y][i]
                    liczba = random.randint(1, kartka[y])
                    while x < liczba:
                        i += 1
                        x += kartkastat[y][i]
                    liczba = random.randint(1, 20)
                    kartkailo[y][i] += 1
                    kartka[y] -= kartkastat[y][i]
                    kartkastat[y][i] = kartkastat[y][i] // 2
                    kartka[y] += kartkastat[y][i]
                    if (liczba == 1 or kartkailo[y][i] == 2):
                        wynik += f"{minuta_str}' {pilkarze[y][i]}  :czerwona_kartka: {logo[y]}\n"
                        usun_zawodnika(y, i)
                        oblicz_szanse()
                        if (kartkailo[y][i] == 2):
                            ocena[y][i] -= random.randint(5, 15) / 10
                            kontuzja(z, 1, 6, 1)
                        else:
                            ocena[y][i] -= random.randint(10, 20) / 10
                            kontuzja(z, 5, 20, 1)
                    else:
                        wynik += f"{minuta_str}' {pilkarze[y][i]}  :zolta_kartka: {logo[y]}\n"
                        ocena[y][i] -= random.randint(1, 5) / 10
                        kontuzja(z, 1, 6, 1)
            # kontuzja
            elif liczba == 6:
                kontuzja(y, 1, 5, 0)
            # oceny i posiadanie piłki
            if minuta % 10 == 0:
                oblicz_posiadanie_pilki()
                for i in range(11):
                    los = random.randint(0, 100)
                    rozovr = ovr[y][i] - sredni_ovr
                    if rozovr >= 0:
                        if rozovr > 10:
                            rozovr = 10
                        if los <= 50:
                            ocena[y][i] += 0
                        elif los <= 65 + rozovr:
                            ocena[y][i] += 0.1
                        elif los <= 80 - rozovr:
                            ocena[y][i] -= 0.1
                        elif los <= 90 + rozovr:
                            ocena[y][i] += 0.2
                        elif los <= 100 - rozovr:
                            ocena[y][i] -= 0.2
                    else:
                        rozovr = abs(rozovr)
                        if rozovr > 10:
                            rozovr = 10
                        elif los <= 65 + rozovr:
                            ocena[y][i] -= 0.1
                        elif los <= 80 - rozovr:
                            ocena[y][i] += 0.1
                        elif los <= 90 + rozovr:
                            ocena[y][i] -= 0.2
                        elif los <= 100 - rozovr:
                            ocena[y][i] += 0.2


# ====================================================================================================#
# ====================================== GLOWNY PROGRAM ==============================================#
# ====================================================================================================#
typ_meczu = druzyny_plik.readline().split()[0]
bonus_boiska = int(druzyny_plik.readline().split()[0])
wynik_dwumeczu = list(map(int, druzyny_plik.readline().split()[:2]))
for nr in range(2):
    temp = druzyny_plik.readline().strip().split()
    nazwa[nr] = " ".join(str(x) for x in (temp[:-1]))
    logo[nr] = temp[-1]
    temp = druzyny_plik.readline().strip().split()
    trenerzy[nr] = " ".join(str(x) for x in (temp[:-3]))
    for i in range(3):
        trener_ovr[nr][i] = int(temp[i - 3])
    for i in range(11):
        temp = druzyny_plik.readline().strip().split()
        pilkarz = " ".join(str(x) for x in (temp[:-2]))
        dodaj_zawodnika(nr, pilkarz, temp[-2], temp[-1], i)
oblicz_szanse()
for i in range(50):
    akcja_meczowa()
stat_pos_pilki = round(posiadanie[0] / (posiadanie[0] + posiadanie[1]) * 100, 2)
koncowy_wynik = ''
koncowy_wynik += f'**{nazwa[0]}** {logo[0]} `{gole[0]}:{gole[1]}` **{nazwa[1]}** {logo[1]}\n'
koncowy_wynik += f'`posiadanie piłki:` {stat_pos_pilki}% - {100 - stat_pos_pilki}%\n'
koncowy_wynik += wynik
for j in range(2):
    koncowy_wynik += f'\n__{nazwa[j]}__{logo[j]} [`trener:` {trenerzy[j]}]'
    for i in range(11):
        if ((ocena[j][i] == max(ocena[j]) and min(gole[0], gole[1]) < gole[j]) or (
                ocena[j][i] == max(max(ocena[0]), max(ocena[1])) and gole[0] == gole[1])): status[j][i] += " :star:"

        koncowy_wynik += f'\n`{poz[j][i]}:` {pilkarze[j][i]} - {round(ocena[j][i], 2)} {status[j][i]}'
    for x in zmienieni:
        if (x[0] == j): koncowy_wynik += f'\n{x[1]} - {round(x[2], 2)}'
# print(f'\n{koncowy_wynik}')
wynik_plik.write(koncowy_wynik)
