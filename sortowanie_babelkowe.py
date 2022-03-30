
ciag = [5, 1, -30, 42, 0, 2, -100]
print(ciag)

for i in range(len(ciag)):
    for j in range(len(ciag)-1-i):
        if ciag[j] > ciag[j+1]:
            ciag[j], ciag[j+1] = ciag[j+1], ciag[j]

        print(ciag)

print(ciag)
