n = int(input("Nhap so luong so Fibon can tao: "))
fibonacci_list = [0, 1] if n >= 2 else [0] if n == 1 else []
for i in range(2, n):
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
print("Danh sach Fibonacci gom", n, "so thu nhat la:")
print(fibonacci_list)
so_nguyen_to = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print("Danh sach cac so nguyen to be hon 100 la :")
print(so_nguyen_to)