n = int(input("Nhap vao phan tu cua mang: "))
arr = []
for i in range(n):
    so = int(input(f"Nhap phan tu thu {i+1}: "))
    arr.append(so)
print("Cac so nguyen to trong mang la:")
for so in arr:
    so_nguyen_to = True
    if so <= 1:
        so_nguyen_to = False
    else:
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                so_nguyen_to = False
                break
    if so_nguyen_to:
        print(so)

print("Cac so hoan hao trong mang la:")
for so in arr:
    so_hoan_hao = False
    if so > 1:
        tong_uoc = 1
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                tong_uoc += i
                if i != so // i:
                    tong_uoc += so // i
        if tong_uoc == so:
            so_hoan_hao = True
    if so_hoan_hao:
        print(so)
