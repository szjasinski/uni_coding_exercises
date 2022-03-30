
Y = [3, 2, 5, 0, 9]
X = [3, 2, 5]


def h(x):
    liczba = 0
    count = 1
    for n in reversed(x):
        liczba += n*count
        count *= 10
    return liczba


# w = h(X)
# for i in X:
#     if w == h(Y[i:m+j]):
#         if X == Y[i:m+i]:

w = h(X)
hY = h(Y[0:m])

for i in range(len(Y)-1);
    hY = (hY - Y[i]*10**m)*10+Y[m+i]
    if w == hY:
        if X == Y[i:m+i]:
            