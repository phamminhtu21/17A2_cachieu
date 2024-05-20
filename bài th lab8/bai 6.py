def loc_so_le(danh_sach):
    return list(filter(lambda x: x % 2 != 0, danh_sach))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cac_so_le = loc_so_le(danh_sach)
print("cac so le co trong danh sach :", cac_so_le)

def loc_so_chan(danh_sach):
    return list(filter(lambda x: x % 2 == 0, danh_sach))

cac_so_chan = loc_so_chan(danh_sach)
print("cac so chan co trong danh sach :", cac_so_chan)

def lap_phuong_danh_sach(danh_sach):
    return list(map(lambda x: x**3, danh_sach))

danh_sach_lap_phuong = lap_phuong_danh_sach(danh_sach)
print("danh sach lap phuong:", danh_sach_lap_phuong)

def loc_va_lap_phuong_so_chan(danh_sach):
    cac_so_chan = filter(lambda x: x % 2 == 0, danh_sach)
    lap_phuong_so_chan = map(lambda x: x**3, cac_so_chan)
    return list(lap_phuong_so_chan)

so_chan_lap_phuong = loc_va_lap_phuong_so_chan(danh_sach)
print("danh sach lap phuong cac so chan :", so_chan_lap_phuong)

def loc_va_binh_phuong_so_le(danh_sach):
    so_le = filter(lambda x: x % 2 != 0, danh_sach)
    binh_phuong_so_le = map(lambda x: x**2, so_le)
    return list(binh_phuong_so_le)

so_le_binh_phuong = loc_va_binh_phuong_so_le(danh_sach)
print("danh sach binh phuong cua cac so le :", so_le_binh_phuong)
