import random

y = [random.randint(0, 10) for x in range(300)]
x = [1, 2]

count = 0
for i in range(len(y)-1):
    if y[i] == x[0] and y[i+1] == x[1]:
        count += 1

print(count)

