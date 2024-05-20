warehouse={
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

hoa_don={}
tong_so_tien=0

for mat_hang in warehouse:
    so_luong=warehouse[mat_hang]
    don_gia=gia_tien[mat_hang]
    thanh_tien=so_luong*don_gia
    hoa_don[mat_hang]={
        "so_luong":so_luong,
        "don_gia":don_gia,
        "thanh_tien":thanh_tien
    }
    tong_so_tien+=thanh_tien

print("hoa don mua hang :")
for mat_hang, thong_tin in hoa_don.items():
    print(f"mat hang:{mat_hang}")
    print(f"So luong:{thong_tin['so_luong']}")
    print(f"don gia:{thong_tin['don_gia']}dong")
    print(f"So tien:{thong_tin['thanh_tien']}dong\n")

print(f"tong so tien cua hoa don : {tong_so_tien}dong")

print("\n so luong mat hang con trong warehouse:")
for mat_hang,so_luong in warehouse.items():
    print(f"{mat_hang}:{so_luong}")