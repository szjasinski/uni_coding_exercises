#najwiekszy mozliwy iloczyn trzech liczb ciagu

start = [2, 1, 4, 2, 4, 5]

# max_iloczyn = 0
# count = 1
# for i in range(len(start)):
#     count += 1
#     for j in range(i, len(start)):
#         count += 1
#         for k in range(j, len(start)):
#             count += 1
#             if i != j and j != k and start[i] * start[j] * start[k] > max_iloczyn:
#                 count += 2 + 2 + 2 + 1 + 3
#                 max_iloczyn = start[i] * start[j] * start[k]
#                 count += 2 + 3


max_iloczyn = 0
count = 1
for i in range(len(start)):
    count += 1
    for j in range(i+1, len(start)):
        count += 1
        for k in range(j+1, len(start)):
            iloczyn = start[i] * start[j] * start[k]
            count += 1 + 3
            if iloczyn > max_iloczyn:
                max_iloczyn = iloczyn
                count += 1
            count += 1


print(max_iloczyn)
print(count)







