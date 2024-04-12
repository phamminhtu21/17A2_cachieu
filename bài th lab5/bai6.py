chuoi_van_ban = input("Nhap chuoi van ban: ")
ky_tu_dac_biet = {}
for ky_tu in chuoi_van_ban:
    if not ky_tu.isalnum():
        if ky_tu in ky_tu_dac_biet:
            ky_tu_dac_biet[ky_tu] += 1
        else:
            ky_tu_dac_biet[ky_tu] = 1
tong_so_ky_tu = len(chuoi_van_ban)
for ky_tu, so_lan_xuat_hien in ky_tu_dac_biet.items():
    print(f"Ky tu '{ky_tu}' xuat hien {so_lan_xuat_hien} lan trong chuoi,tuong ung voi {so_lan_xuat_hien/tong_so_ky_tu*100:.2f}%")
