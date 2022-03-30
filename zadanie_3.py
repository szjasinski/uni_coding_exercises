

def ciag_rek(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * ciag_rek(n-1) + ciag_rek(n-2)
    else:
        return 2 * ciag_rek(n-1) - 3 * ciag_rek(n-2)


ciag = [ciag_rek(i) for i in range(20)]


def parzyste(ciag, n, k):
    if len(ciag) > k/2:
        ciag.pop(k-n)
        return parzyste(ciag, n-1, k)
    return ciag


print(parzyste(ciag, len(ciag), len(ciag)))
