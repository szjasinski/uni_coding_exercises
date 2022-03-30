ciag_wst = []
ciag_wyb = []

dlugosc_ciagu = int(input("podaj długość ciągu: "))

for i in range(dlugosc_ciagu):
    element = int(input("podaj element ciągu: "))
    ciag_wst += [element]
    ciag_wyb += [element]

# sortowanie przez wybieranie
count_wyb = 0
for j in range(dlugosc_ciagu):
    index_min = j
    count_wyb += 2
    for i in range(j, dlugosc_ciagu):
        count_wyb += 1 + 3
        if ciag_wyb[i] < ciag_wyb[index_min]:
            index_min = i
            count_wyb += 1

    temp = ciag_wyb[j]
    ciag_wyb[j] = ciag_wyb[index_min]
    ciag_wyb[index_min] = temp
    count_wyb += 2 + 3 + 2



# sortowanie przez wstawianie
count_wst = 0
for i in range(1, dlugosc_ciagu):
    a = ciag_wst[i]
    j = i - 1
    count_wst += 1 + 2 + 2
    while a < ciag_wst[j] and j >= 0:
        count_wst += 4
        ciag_wst[j+1] = ciag_wst[j]
        ciag_wst[j] = a
        j -= 1
        count_wst += 4 + 2 + 1
    count_wst += 4


print("Algorytm sortowania przez wybieranie wykonał", count_wyb, "operacji prostych.")
print("Algorytm sortowania przez wstawianie wykonał", count_wst, "operacji prostych.")

if count_wyb > count_wst:
    print("Sortowanie przez wstawianie było szybsze.")
elif count_wyb == count_wst:
    print("Żaden program nie był szybszy od innego. ")
else:
    print("Sortowanie przez wybieranie było szybsze. ")

# dla [4, 3, 2, 1] sortowanie przez wybieranie jest szybsze
# dla [2, 1, 4, 3] sortowanie przez wstawianie jest szybsze
