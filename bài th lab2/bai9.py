import math
a,b,c = map(int, input("Nhap he so phuong trinh duong thang (D):ax + by + c = 0 : ").split())
c,d = map(int, input("toa do tam duong tron: ").split())
r = int(input("Ban kinh duong tron : "))

khoang_cach = (abs(a*c + b*d + c)) / (math.sqrt((a**2) + (b**2)))

if khoang_cach == r:
    print("Duong thang txuc duong tron")
elif khoang_cach < r:
    print("Duong thang cat duong tron")
else:
    print("Duong thang nam ngoai duong tron")