chuoi1 = input("Nhap chuoi thu nhat: ")
chuoi2 = input("Nhap chuoi thu hai: ")
matrix = [[0] * (len(chuoi2) + 1) for _ in range(len(chuoi1) + 1)]
do_dai_lon_nhat = 0
vi_tri_cuoi_cung = 0
for i in range(1, len(chuoi1) + 1):
    for j in range(1, len(chuoi2) + 1):
        if chuoi1[i - 1] == chuoi2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
            if matrix[i][j] > do_dai_lon_nhat:
                do_dai_lon_nhat = matrix[i][j]
                vi_tri_cuoi_cung = i
        else:
            matrix[i][j] = 0
if do_dai_lon_nhat == 0:
    print("Khong co chuoi chung.")
else:
    vi_tri_bat_dau = vi_tri_cuoi_cung - do_dai_lon_nhat
    chuoi_con_chung_ngan_nhat = chuoi1[vi_tri_bat_dau:vi_tri_cuoi_cung]
    print("Chuoi ky tu con chung co ky tu ngan nhat:", chuoi_con_chung_ngan_nhat)