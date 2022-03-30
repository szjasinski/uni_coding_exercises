album = [1, 1, 5, 6, 9, 1, 4]

ciag_do_posortowania = [12, 2, 1, 32, 2, 3, 0, 5]

numbers_in_album = []
numbers_not_in_album = []

# rozdzielenie liczb do posortowania na dwie listy
for n in ciag_do_posortowania:
    if n in album:
        numbers_in_album.append(n)
    else:
        numbers_not_in_album.append(n)

# sortowanie rosnaco
for i in range(1, len(numbers_in_album)):
    a = numbers_in_album[i]
    j = i - 1
    while a < numbers_in_album[j] and j >= 0:
        numbers_in_album[j+1], numbers_in_album[j] = numbers_in_album[j], a
        j -= 1

# sortowanie malejaco
for i in range(1, len(numbers_not_in_album)):
    a = numbers_not_in_album[i]
    j = i - 1
    while a > numbers_not_in_album[j] and j >= 0:
        numbers_not_in_album[j+1], numbers_not_in_album[j] = numbers_not_in_album[j], a
        j -= 1

output = numbers_in_album + numbers_not_in_album
print(output)

