s = int(input("Nhap vao so phan tu: "))
arr = []
for i in range(s):
    phan_tu = int(input(f"Nhập phan tu thu {i+1}: "))
    arr.append(phan_tu)
tong_chan = 0
tong_le = 0
for so in arr:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so
print("Tong cac so chan trong mang :", tong_chan)
print("Tong cac so le trong mang:", tong_le)