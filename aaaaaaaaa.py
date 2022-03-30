import random
import math


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

p = random.randint(1, 12)
print("p", p)


def program(n, m):
    print(n)
    if p == n:
        print("koniec")

    k = math.ceil(n/2)
    if p > lista[k]:
        program(math.ceil(3/2*k))
    else:
        program(math.ceil(2/3*k))




# program(len(lista), len(lista))


def funckja(i, j):
    if i == j:
        return lista[i]
    if i + 1 == j:
        return lista[i]
    if lista[(i+j)//2] > p:
        return funckja(i, (i+j)//2)
    else:
        return funckja((i+j)//2, j)


print(funckja(0, len(lista)-1))
