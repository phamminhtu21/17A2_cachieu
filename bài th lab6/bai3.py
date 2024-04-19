s = input("Nhap danh sach cac so cach nhau boi hai dau cach: ")
s = [float(x) for x in s.split()]
gtln = s[0]
gtnn = s[0]
for num in s:

    if num > gtln:
        gtln = num
    
    if num < gtnn:
        gtnn = num
print("GTLN la :", gtln)
print("GTNN la :", gtnn)