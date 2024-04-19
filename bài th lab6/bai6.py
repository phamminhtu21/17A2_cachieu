#bai 6.1
m = int(input("Nhap so hang cua ma tran: "))
n = int(input("Nhap so cot cua ma tran: "))

matran = []
print("Nhap cac phan tu cua ma tran:")
for i in range(m):
    row = []
    for j in range(n):
        yeu_to = int(input(f"Phan tu [{i+1}][{j+1}]: "))
        row.append(yeu_to)
    matran.append(row)

tong_matran = 0
for row in matran:
    tong_matran += sum(row)

print("Tong cua cac phan tu trong ma tran la:", tong_matran)

print("Nhap ma tran thu 2:")
matran2 = []
for i in range(m):
    row = []
    for j in range(n):
        yeu_to = int(input(f"Phần tử [{i+1}][{j+1}]: "))
        row.append(yeu_to)
    matran2.append(row)

sp_matran = []
if len(matran[0]) == len(matran2):
    for i in range(m):
        row = []
        for j in range(len(matran2[0])):
            yeu_to = 0
            for k in range(len(matran2)):
                yeu_to += matran[i][k] * matran[k][j]
            row.append(yeu_to)
        sp_matran.append(row)
    print("Tich cua hai ma tran la :")
    for row in sp_matran:
        print(row)
else:
    print("Hai ma tran khong the nhan vi so cot cua ma tran 1 khong bang so hang ma tran 2.")

chuyendoi_matran = [[matran[j][i] for j in range(m)] for i in range(n)]
print("Ma tran chuyen vi cua ma tran 1 la:")
for row in chuyendoi_matran:
    print(row)





#bai 6.2
n = int(input("Nhap kich thuoc ma tran vuong: "))

print("Nhap cac phan tu ma tran vuong:")
matran = []
for i in range(n):
    row = []
    for j in range(n):
        yeu_to = float(input(f"Phan tu [{i+1}][{j+1}]: "))
        row.append(yeu_to)
    matran.append(row)

dinh_thuc = matran[0][0] * matran[1][1] - matran[0][1] * matran[1][0]
if dinh_thuc == 0:
    print("Ma tran nay khong co ma tran nghich dao vi dinh thuc = 0!")
else:
    nghichdao_matran = [[matran[1][1] / dinh_thuc, -matran[0][1] / dinh_thuc],
                      [-matran[1][0] / dinh_thuc, matran[0][0] / dinh_thuc]]
    print("Ma tran nghich dao cua ma tran da nhap la :")
    for row in nghichdao_matran:
        print(row)

doi_xung = True
for i in range(n):
    for j in range(i + 1, n):
        if matran[i][j] != matran[j][i]:
            doi_xung = False
            break
    if not doi_xung:
        break

if doi_xung:
    print("Ma tran da nhap la ma tran dxung.")
else:
    print("Ma tran ko phai ma tran doi xung.")