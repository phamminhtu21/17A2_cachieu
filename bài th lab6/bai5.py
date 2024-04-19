n= input("Nhap mot danh sach so nguyen cach nhau bang hai dau cach: ")
n = [int(x) for x in n.split()]

if len(n) < 3:
    print("Danh sach khong tao thanh day so hoc.")
else:
    diff  = n[1] - n[0]
    for i in range(2, len(n)):
        if n[i] - n[i-1] != diff:
            print("Danh sach khong tao thanh day so hoc.")
            break
    else:
        print("Danh sach tao thanh day so hoc voi cong sai co dinh ", diff)
        print("Danh sach la :", n)
