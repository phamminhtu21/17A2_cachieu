chuoi1 = input("Nhap chuoi ky tu 1: ")
chuoi2 = input("Nhap chuoi ky tu 2: ")
do_dai_chuoi1 = len(chuoi1)
do_dai_chuoi2 = len(chuoi2)
chuoi_ket_qua = ""
do_dai_lon_nhat = max(do_dai_chuoi1, do_dai_chuoi2)
for i in range(do_dai_lon_nhat):
    if i < do_dai_chuoi1:
        chuoi_ket_qua += chuoi1[i]
    if i < do_dai_chuoi2:
        chuoi_ket_qua += "-" + chuoi2[i]
print("Ket qua sau khi tron 2 chuoi:", chuoi_ket_qua)