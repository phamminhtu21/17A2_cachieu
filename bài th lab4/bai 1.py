# a)
tong = 0 
so = 0 
while tong <= 1000:
    n = int(input("Nhap mot so n : "))
    so = so + 1
    if n % 2 != 0 :
        tong+=n
    print(tong)

# b)
tong = 0
so_b = 0
while tong <= 1000 :
    n = int(input("Nhap mot so n: "))
    so = so + 1
    if n%2 == 0 :
        tong+=n
    print(tong)

# c)
print(f"So luong so nguyen nhap vao : {so+so_b}")