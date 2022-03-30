

def zdaje_zdalnie_rek(A, p):
    n = len(A)
    if p == n:
        return A[p-1]
    q = zdaje_zdalnie_rek(A, p+1)
    if A[p-1] <= q:
        return A[p-1]
    return q


def zdaje_zdalnie_iter(A, p):
    n = len(A)




A = [1, 2, 3, 4, 5, 6, 7]

print(zdaje_zdalnie_rek(A, 1))
