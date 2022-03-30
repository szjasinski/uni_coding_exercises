the_list = [2137, 1000000, 1, -3, 5, 420, 6, 9, 1, 4, -99, 69, 33]


print(the_list)

for i in range(1,d):
    a=lista[i]
    j=i-1
    while (a<lista[j]) and (j>=0):
        lista[j+1]=lista[j]
        j=j-1
        lista[j+1]=a


# for i in range(1, len(the_list)):
#     a = the_list[i]
#     j = i - 1
#     while a < the_list[j] and j >= 0:
#         the_list[j+1] = the_list[j]
#         the_list[j] = a
#         j -= 1


# sortowanie rosnaco
for i in range(1, len(the_list)):
    a = the_list[i]
    j = i - 1
    while a < the_list[j] and j >= 0:
        the_list[j+1], the_list[j] = the_list[j], a
        j -= 1

# sortowanie malejaco
for i in range(1, len(the_list)):
    a = the_list[i]
    j = i - 1
    while a > the_list[j] and j >= 0:
        the_list[j+1], the_list[j] = the_list[j], a
        j -= 1


for i in range(1,d):
    a=lista[i]
    j=i-1
    while (a<lista[j]) and (j>=0):
        lista[j+1]=lista[j]
        j=j-1
        lista[j+1]=a


print(the_list)


for i, n in enumerate(the_list):
    break