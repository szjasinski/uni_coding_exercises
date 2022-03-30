# sortowanie przez wybieranie

ciag_wyb = [9, -45, 0, 2, 3]
dlugosc_ciagu = len(ciag_wyb)

for j in range(dlugosc_ciagu):
    print(j)
    index_min = j
    for i in range(j, dlugosc_ciagu):
        if ciag_wyb[i] < ciag_wyb[index_min]:
            index_min = i

            temp = ciag_wyb[j]
            ciag_wyb[j] = ciag_wyb[index_min]
            ciag_wyb[index_min] = temp

            print("i: ", i, ", index_min: ", index_min)
            print(ciag_wyb)

print(ciag_wyb)