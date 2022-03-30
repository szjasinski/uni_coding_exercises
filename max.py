
given_list = []
l = int(input('Podaj liczbę elementów listy:'))

if l > 0:
    for n in range(l):
        given_number = int(input('Podaj liczbę:'))
        given_list.append(given_number)

    max = given_list[0]
    for n in given_list:
        if n > max:
            max = n
    print(max)
else:
    print("lista nie może być pusta")
