n=0
for i in range(2000,4001):
    if i%7==0 and i%5!=0:
        n+=i
print("Tổng là:",n)