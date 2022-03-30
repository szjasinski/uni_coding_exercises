
ciag_liczb = []


def wpisz_liczbe():
    a = input("podaj liczbe: ")
    if a == "stop":
        print(ciag_liczb)
    else:
        ciag_liczb.append(int(a))
        wpisz_liczbe()



wpisz_liczbe()