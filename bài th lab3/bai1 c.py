n=int(input("Nhập số nguyên:"))
import math
S3=0
for i in range(1,n+1):
    if n<=0:
        print("Vui lòng nhập lại")
    else:
        S3+=1/math.sqrt(i*2)
print("Tổng của S3 là: ",S3)