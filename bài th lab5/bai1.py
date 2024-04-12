so_thap_phan = int(input("Nhap so nguyen (so thap phan): "))
so_nhi_phan = ""
while so_thap_phan > 0:
    du = so_thap_phan % 2
    so_nhi_phan = str(du) + so_nhi_phan
    so_thap_phan = so_thap_phan // 2
print("So nhi phan tuong ung :", so_nhi_phan)