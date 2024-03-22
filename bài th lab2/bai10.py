print('''The loai:
            1. Phim hanh dong
            2. Phim kinh di
            3. Phim tinh cam
            4. Phim hai huoc
            5. Phim hoat hinh
        ''')

chon = int(input("lua chon phim : "))
thoi_gian = input("Nhập thời gian muốn xem phim (sáng, trưa, chiều, tối): ")

if chon == 1:
    if thoi_gian == "sáng" or thoi_gian == "trưa" or thoi_gian== "chiều" or thoi_gian == "tối":
        print("Phim hành động được chiếu vào mọi khung giờ trong ngày")
elif chon == 2:
    if thoi_gian == "tối":
        print("Có suất chiếu phim kinh dị")
    else:
        print("Không có suất chiếu")
elif chon == 3:
    if thoi_gian == "tối":
        print("Có suất chiếu phim tình cảm")
    else:
        print("Phim tình cảm chỉ được chiếu vào buổi tối")
elif chon == 4:
    if thoi_gian == "sáng" or thoi_gian == "trưa" or thoi_gian == "chiều" or thoi_gian == "tối":
        print("Phim hài hước được chiếu vào mọi khung giờ trong ngày")
else:
    if thoi_gian == "tối" or thoi_gian == "chiều":
        print("Không có suất chiếu")
    else:
        print("Có suất chiếu phim hoạt hình")   