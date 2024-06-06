import random
import csv
ket_qua = ["Bang", "Click"]
xac_suat = {"Bang": 0.4, "Click": 0.6}
tap_ket_qua = set(ket_qua)
def lac_sung():
    gia_tri_ngau_nhien = random.random()
    xac_suat_tich_luy = 0.0
    for kq in ket_qua:
        xac_suat_tich_luy += xac_suat[kq]
        if gia_tri_ngau_nhien < xac_suat_tich_luy:
            return kq
    return ket_qua[-1]
def tinh_xac_suat(ket_qua_lac):
    tong_so_lan = len(ket_qua_lac)
    dem_so_lan = {kq: ket_qua_lac.count(kq) for kq in tap_ket_qua}
    xac_suat_thuc_te = {kq: so_lan / tong_so_lan for kq, so_lan in dem_so_lan.items()}
    return xac_suat_thuc_te
def luu_vao_csv(ket_qua_lac, xac_suat_thuc_te, ten_file="ket_qua_lac_sung.csv"):
    with open(ten_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Ket Qua", "So Lan", "Xac Suat"])
        dem_so_lan = {kq: ket_qua_lac.count(kq) for kq in tap_ket_qua}
        for kq in tap_ket_qua:
            writer.writerow([kq, dem_so_lan[kq], xac_suat_thuc_te[kq]])
def mo_phong(so_lan):
    ket_qua_lac = []
    for _ in range(so_lan):
        ket_qua = lac_sung()
        ket_qua_lac.append(ket_qua)
    return ket_qua_lac
def main():
    for i in range(5):
        ket_qua_lac = mo_phong(1)
        print(f"So lan lac sung{i+1}: {ket_qua_lac[-1]}")
    tong_so_lan = 500
    ket_qua_lac = mo_phong(tong_so_lan)
    dem_so_lan = {kq: ket_qua_lac.count(kq) for kq in tap_ket_qua}
    xac_suat_thuc_te = tinh_xac_suat(ket_qua_lac)
    print(f"\nTong kq sau {tong_so_lan} lần lắc:")
    for kq, so_lan in dem_so_lan.items():
        print(f"{kq}: {so_lan} lần")
    print("\n Ti le xuat hien cua tung kq:")
    for kq, xs in xac_suat_thuc_te.items():
        print(f"{kq}: {xs:.2%}")
    luu_vao_csv(ket_qua_lac, xac_suat_thuc_te)
if __name__ == "__main__":
    main()
