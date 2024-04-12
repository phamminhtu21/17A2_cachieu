n1 = input("Chuoi 1: ")
n2 = input("Chuoi 2: ")
if len(n1) == len(n2):
    differences = 0
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            differences += 1
    if differences <= 2:
        print("Co the thay doi tu chuoi 1 thanh chuoi 2.")
    else:
        print("Khong the thay doi.")
else:
    print("Khong the thay doi vi do dai 2 chuoi khong giong nhau.")
