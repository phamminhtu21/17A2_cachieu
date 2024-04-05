# a)
n=2
while n<100:
    check=True
    b=2
    while b**2<=n:
        if n%b== 0:
            check=False
            break
        b+= 1
    if check==True:
        print(n, end=" ")
    n+= 1

# b)
a=1
while a<100:
    b=int(a**0.5)
    if b**2==a:
        print(a,end=" ")
    a+=1         

#c)
a, b = 0, 1
print(a)
while b < 1000:
    print(b)
    a, b = b, a + b