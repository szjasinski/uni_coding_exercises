import matplotlib.pyplot as plt


def ta_liczba(n):
    ciag_liczb = ["1", "2"]
    licznik = 3

    for element in ciag_liczb:
        licznik += 1 + 2
        if len(ciag_liczb) < n:
            for cyfra in ["1", "2"]:
                nowa_liczba = element + cyfra
                ciag_liczb.append(nowa_liczba)
                licznik += 4 + 2 + 1

        else:
            break

    licznik += 3
    return int(ciag_liczb[n-1]), licznik


lista_n = [n for n in range(3, 1000)]
lista_licznika = [ta_liczba(n)[1] for n in range(3, 1000)]
lista_tej_liczby = [ta_liczba(n)[0] for n in range(3, 1000)]

lista_8x = [8*n for n in range(3, 1000)]

# print(ta_liczba(10000)[0])
# print(ta_liczba(10000)[1])

plt.plot(lista_n, lista_licznika, 'ro')
plt.plot(lista_n, lista_8x, 'yo')
# plt.plot(lista_n, lista_tej_liczby, 'bo')

print(lista_tej_liczby)

plt.show()





# def ta_liczba(n):
#     ciag_liczb = ["1", "2"]
#
#     for element in ciag_liczb:
#         if len(ciag_liczb) < n:
#             for cyfra in ["1", "2"]:
#                 nowa_liczba = element + cyfra
#                 ciag_liczb.append(nowa_liczba)
#
#         else:
#             break
#
#     print(ciag_liczb)
#     return int(ciag_liczb[n - 1])
#
#
# print(ta_liczba(10000))
#
