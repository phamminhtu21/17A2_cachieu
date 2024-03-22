chieu_cao=float(input("Nhap vao chieu cao:"))
can_nang=int(input("Nhap vao can nang:"))
BMI=can_nang/(chieu_cao**2)
print("Chi so BMI của ban",BMI)
if BMI<18.5:
    print("Gay")
elif BMI>=18.5 and BMI<25:
    print("Binh thuong")
elif BMI>=25 and BMI<30:
    print("Hoi beo")
elif BMI>=30:
    print("Beo ")