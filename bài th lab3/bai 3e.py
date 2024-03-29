i = 0

for n in range(1, 201):
    number = n * (3 * n - 1) // 2
    i += number

print("Tổng của các số ngũ giác từ 1 đến 200 là:", i)