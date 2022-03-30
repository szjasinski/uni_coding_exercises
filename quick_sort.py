

def quick_sort(a):
    if len(a) > 1:
        k = a[0]
        L = [x for x in a if x <= k]
        R = [x for x in a if x > k]
        quick_sort(L)
        quick_sort(R)
        print(L, R)


quick_sort([1, 2, 3, 1])