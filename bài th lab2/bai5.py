so_nguoi=int(input("Nhap vao so nguoi:"))
gia_ve=120000
if so_nguoi>=2 and so_nguoi<=4:
    so_tien= (gia_ve-(gia_ve*0.05))*so_nguoi
    print("so tien phai tra",so_tien)
elif so_nguoi>=4 and so_nguoi<=10:
    so_tien= (gia_ve-(gia_ve*0.05))*so_nguoi
    print("so tien phai tra",so_tien)
elif so_nguoi>10:
    so_tien= (gia_ve-(gia_ve*0.05))*so_nguoi
    print("so tien phai tra",so_tien)
else: 
    so_tien=so_nguoi*gia_ve
    print("so tien phai tra",so_tien)
