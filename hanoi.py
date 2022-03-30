
ciag1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ciag2 = []
ciag3 = []


def przenies(a, b):
    if len(a) > 0 and len(b) > 0:
        if a[len(a)-1] > b[len(b)-1]:
            b.append(a[len(a)-1])
            a.pop()
        else:
            print('nie można przełożyć')
    elif len(a) > 0:
        b.append(a[len(a)-1])
        a.pop()
    else:
        print('nie ma czego przekladac')
    return a, b


def hanoi__3(a, b, c):
    a, c = przenies(a, c)
    a, b = przenies(a, b)
    c, b = przenies(c, b)
    a, c = przenies(a, c)
    b, a = przenies(b, a)
    b, c = przenies(b, c)
    a, c = przenies(a, c)
    print(a, b, c)


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        przenies(a, c)
        hanoi(n-1, b, a, c)


print(ciag1, ciag2, ciag3)
# hanoi__(ciag1, ciag2, ciag3)
hanoi(10, ciag1, ciag2, ciag3)
print(ciag1, ciag2, ciag3)
