
a = [1, 5, 12, 54, 0, 6, 8, 121, 8, 9, -1000, 7, 70, -7]

# parzyste liczby
even_number_list = []
for n in a:
    if n % 2 == 0:
        even_number_list.append(n)
        # even_number_list = even_number_list + [n]

# podzielne przez 7
div7_number_list = []
for n in a:
    if n % 7 == 0:
        div7_number_list.append(n)

# parzyste miejsca
even_index_list = []
for n in a:
    if a.index(n) % 2 == 0:
        even_index_list.append(n)

print("even_number_list", even_number_list)
print("div7_number_list", div7_number_list)
print("even_index_list", even_index_list)
