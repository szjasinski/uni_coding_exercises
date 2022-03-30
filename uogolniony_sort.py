
moja_lista = ["      ", "ciag", "spacer", "0", "-300", "$$$$", "2x2", "3", "2", "1", "000000000", "00000000000000", "!@#$%^&*()", "-1", "-1000", "B", "!!", "B"]


def porownaj(a, b):
    sum_a = 0
    sum_b = 0
    for x in a:
        sum_a += ord(x)
    for x in b:
        sum_b += ord(x)
    # print(a, sum_a, b, sum_b)
    if sum_a <= sum_b:
        return True
    return False


def uogolniony_sort(ciag):
    dlugosc = len(ciag)

    for i in range(dlugosc):
        for j in range(dlugosc - 1 - i):
            if porownaj(ciag[j + 1], ciag[j]):
                t = ciag[j]
                ciag[j] = ciag[j + 1]
                ciag[j + 1] = t
    return ciag


def sprawdz(ciag):
    ciag_liczb = []
    for x in ciag:
        wyraz = sum([ord(k) for k in x])
        ciag_liczb.append(wyraz)
    return ciag_liczb


print(sprawdz(moja_lista))
print(uogolniony_sort(moja_lista))
print(sprawdz(uogolniony_sort(moja_lista)))