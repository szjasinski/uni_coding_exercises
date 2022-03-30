

a = 0
b = 1
fibonacci_list = [a, b]
for n in range(999):
    fibo_num = a + b
    a = b
    b = fibo_num
    fibonacci_list.append(fibo_num)
print(fibo_num)
print(fibonacci_list[1000])
