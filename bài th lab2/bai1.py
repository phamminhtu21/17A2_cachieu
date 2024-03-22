a=int(input("Nhap vao so:"))
b=int(input("Nhap vao so:"))
print(f"nghiem phuong trinh bac nhat ax+b=0")
if a==0:
    if b==0:
        print("phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
elif b==0:
    print("Phuong trinh co nghiem x=0 ")
else:
    print("phuong trinh co nghiem:x=",-b/a)