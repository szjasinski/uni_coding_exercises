import random
from itertools import combinations_with_replacement
from itertools import permutations


d = 3
alfabet = [n for n in range(d)]

X_1 = [1, 2]
X_2 = [1, 1]
Y = [random.randint(0, d-1) for n in range(3000)]


def generuj_ciagi(n):
    lista_ciagow = []
    comb = combinations_with_replacement(alfabet, n)
    for ciag in comb:
        if len(set(ciag)) != 1:
            perm = permutations(ciag)
            for x in perm:
                lista_ciagow.append(list(x))
        else:
            lista_ciagow.append(list(ciag))
    return lista_ciagow


def program(x1, x2, y, alfabet):
    wynik1 = 0
    wynik2 = 0

    # wzorce dowolnej dlugosci
    lista_wzorcow_1 = []
    max_znakow = 10 - len(x1) - len(x2)
    for i in range(1, max_znakow):
        nowe_ciagi = generuj_ciagi(i)
        for ciag in nowe_ciagi:
            lista_wzorcow_1.append(x1+ciag+x2)

    for wzorzec in lista_wzorcow_1:
        for i in range(len(y) - len(wzorzec)+1):
            if wzorzec == y[i:i+len(wzorzec)]:
                wynik1 += 1

    # wzorce dlugosci len(x1)+2+len(x2)
    lista_wzorcow_2 = [x1 + [n, m] + x2 for n in alfabet for m in alfabet]
    for wzorzec in lista_wzorcow_2:
        for i in range(len(y) - len(wzorzec)+1):
            if wzorzec == y[i:i+len(wzorzec)]:
                wynik2 += 1

    return wynik1, wynik2


print(program(X_1, X_2, Y, alfabet))


