a,b = map(int, input("Nhap he so duong thang 1: ").split())
c,d = map(int, input("Nhap he so duong thang 2: ").split())

if a != 0 and c != 0:
    if a == c:
        print("Hai duong thang song song")
    elif a != c:
        if a * c == -1:
            print("Hai duong thang vuong goc")
        else:
            print("Hai duong thang cat nhau")
else:
    print("He so goc phai khac 0")     