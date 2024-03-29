i=int(input("Nhập vào số nguyên:"))
S4=0
for i in range(1,n+1):
    if n<=0:
        print("Vui lòng nhập lại") 
    else:
        S4+=((-1)**(i+1))/i
print("Tổng của S3 là: ",S4) 