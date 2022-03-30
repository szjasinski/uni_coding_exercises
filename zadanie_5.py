

def NWW_ciagu():
    n = int(input("podaj ile liczb chcesz wpisac: "))
    if n < 2:
        return "za malo argumentow"

    lista = [int(input("podaj liczbe: ")) for i in range(n)]
    if 0 in lista:
        return "NWW niezdefiniowane"

    s = 1
    for x in lista:
        k = s
        while s % x != 0:
            s += k
    return s


print(NWW_ciagu())
