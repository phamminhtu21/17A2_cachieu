number=int(input("Nhập một số: "))
count=1
a=number
while True:
    a=a//10
    if a==0:
        break
    count+=1

for i in range(count,0,-1):
    phan_nguyen=number//(10**(i-1))
    if phan_nguyen==0:
        print("zero",end=" ")
        number=number%(10**(i-1))
    elif phan_nguyen == 1:
        print("one",end=" ")
        number=number%(10**(i-1))    
    elif phan_nguyen==2:
        print("two",end=" ")
        number=number%(10**(i-1))
    elif phan_nguyen==3:
        print("three",end=" ")
        number=number%(10**(i-1))
    elif phan_nguyen==4:
        print("four", end=" ")
        number=number%(10**(i-1))
    elif phan_nguyen==5:
        print("five",end=" ")
        number=number%(10**(i-1))
    elif phan_nguyen==6:
        print("six",end=" ")
        number=number%(10**(i-1))
    elif phan_nguyen == 7:
        print("seven",end=" ")
        number=number%(10**(i-1))
    elif phan_nguyen==8:
        print("eight",end=" ")
        number=number%(10**(i-1))
    elif phan_nguyen==9:
        print("nine",end=" ")
        number=number%(10**(i-1))