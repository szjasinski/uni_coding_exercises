#program funkcje ktora pozwoli nam scalic dwa ciagi czyli ma dostac dwa ciagi(posortowane) i zwrocic jeden ciag ktory jest suma ich

a = [1, 2, 3, 4, 5, 6, 7]
b = [0, 2, 4, 6, 8, 10, 12]
ciag = []


def scal(a, b, ciag):
    if a and b:
        if a[0] < b[0]:
            ciag.append(a[0])
            a.pop(0)
        else:
            ciag.append(b[0])
            b.pop(0)
        return scal(a, b, ciag)
    ciag += a + b
    return ciag


# print(scal(a, b, []))


def sortowanie_scalanie(a):
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]
        print("L", L, "R", R)
        sortowanie_scalanie(L)
        sortowanie_scalanie(R)
        print(scal(L, R, []))
    return a


def merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2
        L = a[:mid]
        R = a[mid:]
        print("L", L, "R", R)
        merge_sort(L)
        merge_sort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
        print("PO", a)


# merge_sort([4, 6, 2, 1, 0])
# sortowanie_scalanie([4, 6, 2, 1, 0])
