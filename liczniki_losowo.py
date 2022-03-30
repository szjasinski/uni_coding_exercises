import random
import matplotlib.pyplot as plt

lista_licznika1 = []
lista_licznika2 = []
lista_licznika3 = []

dlugosc_ciagu = 100

lista_n = []
for n in range(dlugosc_ciagu):
    lista_n += [n]


for dlugosc in lista_n:
    ciag_wyb = []
    ciag_wst = []
    ciag_bab = []

    for x in lista_n:
        ciag_wyb.append(random.randint(0, 100))
        ciag_wst.append(ciag_wyb[x])
        ciag_bab.append(ciag_wyb[x])


    # sortowanie przez wybieranie
    licznik1 = 0
    for j in range(dlugosc):
        index_min = j
        licznik1 += 2
        for i in range(j, dlugosc):
            licznik1 += 1 + 3
            if ciag_wyb[i] < ciag_wyb[index_min]:
                index_min = i
                licznik1 += 1

        temp = ciag_wyb[j]
        ciag_wyb[j] = ciag_wyb[index_min]
        ciag_wyb[index_min] = temp
        licznik1 += 2 + 3 + 2

    # sortowanie przez wstawianie
    licznik2 = 0
    for i in range(1, dlugosc):
        a = ciag_wst[i]
        j = i - 1
        licznik2 += 1 + 2 + 2
        while a < ciag_wst[j] and j >= 0:
            licznik2 += 4
            ciag_wst[j+1] = ciag_wst[j]
            ciag_wst[j] = a
            j -= 1
            licznik2 += 4 + 2 + 1
        licznik2 += 4

    # sortowanie bąbelkowe
    licznik3 = 0
    for i in range(dlugosc):
        licznik3 += 1
        for j in range(dlugosc - 1 - i):
            licznik3 += 1
            licznik3 += 4
            if ciag_bab[j] > ciag_bab[j + 1]:
                t = ciag_bab[j]
                ciag_bab[j] = ciag_bab[j+1]
                ciag_bab[j+1] = t
                licznik3 += 2 + 4 + 3

    lista_licznika1.append(licznik1)
    lista_licznika2.append(licznik2)
    lista_licznika3.append(licznik3)


plt.plot(lista_n, lista_licznika1, 'ro')
plt.plot(lista_n, lista_licznika2, 'bo')
plt.plot(lista_n, lista_licznika3, 'yo')

plt.show()

print(lista_licznika1)
print(lista_licznika2)
print(lista_licznika3)
