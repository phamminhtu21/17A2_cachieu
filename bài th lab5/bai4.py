chuoi_van_ban = input("Nhap chuoi van ban: ")
tu_can_tim = input("Nhap tu can tim: ")
vi_tri = chuoi_van_ban.find(tu_can_tim)
print(f"Vi tri tu '{tu_can_tim}' trong chuoi la: {vi_tri}")
so_lan_xuat_hien = chuoi_van_ban.count(tu_can_tim)
print(f"Tu '{tu_can_tim}' xuat hien {so_lan_xuat_hien} lan trong chuoi")
tu_nhieu_nhat = max(set(chuoi_van_ban.split()), key=chuoi_van_ban.split().count)
print(f"Tu xuat hien nhieu nhat trong chuoi '{tu_nhieu_nhat}'")