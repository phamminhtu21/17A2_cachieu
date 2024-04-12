n = input("Nhap chuoi do dai co hon 10 ky tu: ")
if len(n) > 10:
    substring = n[1:8]
    print("Chuoi ky tu con tu thu 2 den 8:", substring)
else:
    print("Chuoi khong co do dai hon 10 ky tu.")
input_string = input("Nhap chuoi co hon 10 ky tu: ")
if len(input_string) > 10:
    sub_string_b = input_string[4:9]
    print("b) Chuoi ky tu con tu vi tri thu 5 gom 5 ky tu:", sub_string_b)
    sub_string_c = input_string[-3:]
    print("c) Chuoi ky tu con tu cuoi chuoi gom 3 ky tu:", sub_string_c)
    lowercase_string = input_string.lower()
    print("d) Chuoi chu thuong:", lowercase_string)
    uppercase_string = input_string.upper()
    print("e) Chuoi chu hoa:", uppercase_string)
    reversed_string = input_string[::-1]
    print("f) Chuoi ky tu dao nguoc:", reversed_string)
else:
    print("Chuoi ko co do dai hon 10 ky tu.")